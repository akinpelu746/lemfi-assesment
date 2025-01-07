import os
import time
import requests
from prometheus_client import start_http_server, Gauge
from typing import Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "guest")
METRICS_PORT = int(os.getenv("METRICS_PORT", "8000"))
SCRAPE_INTERVAL = int(os.getenv("SCRAPE_INTERVAL", "30"))

QUEUE_MESSAGES = Gauge(
    "rabbitmq_individual_queue_messages",
    "Total number of messages in queue",
    ["host", "vhost", "name"],
)

QUEUE_MESSAGES_READY = Gauge(
    "rabbitmq_individual_queue_messages_ready",
    "Number of messages ready in queue",
    ["host", "vhost", "name"],
)

QUEUE_MESSAGES_UNACKED = Gauge(
    "rabbitmq_individual_queue_messages_unacknowledged",
    "Number of unacknowledged messages in queue",
    ["host", "vhost", "name"],
)


class RabbitMQExporter:
    def __init__(self):
        self.base_url = f"http://{RABBITMQ_HOST}:15672/api"
        self.auth = (RABBITMQ_USER, RABBITMQ_PASSWORD)
        self.session = requests.Session()
        self.session.auth = self.auth

    def get_queue_metrics(self) -> None:
        """Fetch metrics for all queues in all vhosts."""
        try:
            response = self.session.get(f"{self.base_url}/queues")
            response.raise_for_status()
            queues = response.json()

            for queue in queues:
                labels = {
                    "host": RABBITMQ_HOST,
                    "vhost": queue["vhost"],
                    "name": queue["name"],
                }

                QUEUE_MESSAGES.labels(**labels).set(queue["messages"])
                QUEUE_MESSAGES_READY.labels(**labels).set(queue["messages_ready"])
                QUEUE_MESSAGES_UNACKED.labels(**labels).set(
                    queue["messages_unacknowledged"]
                )

            logger.info(f"Successfully collected metrics from {len(queues)} queues")

        except requests.exceptions.RequestException as e:
            logger.error(f"Error collecting RabbitMQ metrics: {str(e)}")
        except (KeyError, ValueError) as e:
            logger.error(f"Error processing queue data: {str(e)}")

    def run_metrics_loop(self) -> None:
        """Main metrics collection loop."""
        while True:
            self.get_queue_metrics()
            time.sleep(SCRAPE_INTERVAL)


def main():
    try:
        start_http_server(METRICS_PORT)
        logger.info(f"Metrics server started on port {METRICS_PORT}")
        exporter = RabbitMQExporter()
        logger.info(f"Starting metrics collection from RabbitMQ at {RABBITMQ_HOST}")
        exporter.run_metrics_loop()

    except Exception as e:
        logger.error(f"Fatal error in main loop: {str(e)}")
        raise


if __name__ == "__main__":
    main()
