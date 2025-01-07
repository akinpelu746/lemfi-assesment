import psutil
import subprocess
import time

# Configuration
SERVICE_NAME = "laravel-backend.service"
CPU_THRESHOLD = 80  # CPU usage percentage threshold
CHECK_INTERVAL = 10  # Interval to check CPU usage in seconds


def restart_service():
    try:
        subprocess.run(["systemctl", "restart", SERVICE_NAME], check=True)
        print(f"{SERVICE_NAME} restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to restart {SERVICE_NAME}: {e}")


def monitor_cpu_usage():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > CPU_THRESHOLD:
            restart_service()
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    monitor_cpu_usage()
