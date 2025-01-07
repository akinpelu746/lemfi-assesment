## Section 1: General Technical Knowledge

### 1. What are the key security concerns when it comes to DevOps?

- **Unrestricted Permissions**: Lack of least privilege enforcement can lead to over-permissioned services and accounts, increasing the risk of unauthorized access.
- **Secrets Management**: Ensuring secure handling of credentials, API keys, and certificates. This includes periodic rotation of secrets to mitigate the risk of long-term exposure.
- **Vulnerabilities**: Scanning for vulnerabilities in the codebase, third-party dependencies, and infrastructure. Implementing least privilege access and conducting regular security audits.
- **Exposure of Secrets**: Secrets should never be hardcoded in the codebase, and special care should be taken to prevent accidental exposure in pipelines or infrastructure-as-code (IaC) configurations.

---

### 2. Designing a Self-Healing Distributed Service:

To design a self-healing distributed system, consider the following:

1. **Deployment on Self-Healing Platforms**: Utilize platforms like Kubernetes or HashiCorp Nomad to automatically replace unhealthy services.
2. **Auto-Scaling**: Combine Horizontal Pod Autoscaler (HPA) and Vertical Pod Autoscaler (VPA) to scale based on CPU and memory usage.
3. **Health Monitoring**: Implement comprehensive health checks for individual services to detect failures, using tools like Prometheus and Grafana for monitoring.
4. **Fault Tolerance**: Ensure that failing services are isolated and do not affect other parts of the system. Service meshes like Istio can help with traffic management.
5. **Circuit Breakers and Retries**: Use service meshes or libraries to implement retries and circuit breakers for transient failures.

---

### 3. Describe a Centralized Logging Solution and How You Can Implement Logging for a Microservice Architecture

A centralized logging solution can be implemented using tools like the **ELK Stack (Elasticsearch, Fluentd, Kibana)** or **Loki** for log aggregation and querying. 

- **Log Collection**: Deploy Fluentd or a similar agent as a DaemonSet in Kubernetes to collect logs from all containers running on nodes.
- **Log Aggregation**: Fluentd processes the logs and sends them to a central log aggregation system like **Elasticsearch** or **Loki**.
- **Log Visualization**: Use **Kibana** or **Grafana** to visualize the logs, making it easier to identify issues across the system.
- **Benefits**: Centralized logging enables better searchability, faster debugging, and correlation of events across microservices.

---

### 4. What are some of the reasons for choosing Terraform for DevOps?

- **State Management**: Terraform tracks the state of infrastructure, allowing you to detect and correct drift by reapplying configuration when changes occur.
- **Multi-cloud Support**: Terraform can deploy infrastructure across multiple cloud providers (AWS, GCP, Azure), making it ideal for hybrid and multi-cloud environments.
- **Infrastructure as Code (IaC)**: Terraform allows you to define and provision infrastructure using declarative code, ensuring consistency and reproducibility.

---

### 5. How would you design and implement a secure CI/CD architecture for microservice deployment using GitOps? (Scenario: 20 microservices with different languages, deploying to Kubernetes)

- **Dockerize Applications**: Containerize each microservice using Docker to ensure consistent deployments.
- **GitOps with ArgoCD**: Use **ArgoCD** to automate the deployment process, ensuring that code changes are automatically deployed to Kubernetes.
- **Secret Management**: Use **Kubernetes External Secrets** to manage secrets in a secure and compliant manner, injecting them into the appropriate namespaces.
- **Environments**: Implement three distinct environments (Dev, Staging, Prod) with separate pipelines:
  - In **Dev**, GitHub Actions or GitLab CI will run tests, linting, build Docker images, and push them to a registry. Kubernetes manifests will be updated with new image tags.
  - **ArgoCD** will automatically sync changes and deploy them to the cluster.
  - After testing in **Dev**, the service will be moved to **Staging** for QA before being promoted to **Prod**.

---

### 6. You notice React Native builds are failing intermittently. What’s your debugging process?

1. **Check Build Logs**: Review the logs to identify specific error messages.
2. **Verify Dependencies**: Ensure that all dependencies are up to date and compatible with each other.
3. **Clean Build Cache**: Clear the build cache and `node_modules` directory to resolve any potential issues with cached files.

---

### 7. Code for Prometheus Exporter
The code can be found in the file `./07_prometheus.exporter.py`.

---

### 8. Code for Laravel CPU Restart
The code can be found in the file `./08_laravel_cpu_restart.py`.

---

### 9. A Postgres Query is Running Slower Than Expected. Explain Your Approach to Troubleshooting It.

1. **Check System Resources**: Investigate system metrics such as CPU usage, memory consumption, IO wait times, and potential swapping.
2. **Analyze Query Execution Plan**: Use `EXPLAIN (ANALYZE, BUFFERS)` to understand the query plan. Focus on the actual vs. estimated row counts, execution time at each step, and buffer usage.
3. **Optimize Query**: Based on the execution plan, consider adding indexes, rewriting inefficient queries, or removing unused indexes.
4. **Check for Dead Tuples**: Verify if there are dead tuples that need vacuuming to improve database performance.

---

### 11. How Would You Set Up Monitoring for the React Native Mobile App’s API Endpoints?

- **Error and Performance Tracking**: Use tools like **Sentry** for error tracking and **Datadog** or **New Relic** for performance monitoring of API endpoints.
- **Metrics**: Track API response times, success/error rates, and user interactions to identify issues early.

---

### 12. Debugging High Latency in Node.js Microservices

1. **Analyze Metrics and Logs**: Investigate slow requests using application logs and metrics.
2. **Profile Code**: Identify potential bottlenecks, such as database queries or slow external API calls.
3. **Scale Horizontally**: If high traffic is causing overloads, increase the number of instances to handle the additional load.

---

### 13. Describe a Time You Improved the Performance of an Infrastructure System. What Challenges Did You Face?

**Situation**: We encountered a traffic surge, and despite Kubernetes auto-scaling, only 50% of requests were successful. This indicated that newly spawned pods were not properly handling the load.

**Task**: Identify the root cause and implement a scalable solution to handle increased traffic without timing out or failing health checks.

**Action**:
- **Analyzed Logs**: Found that requests were queued at the API gateway and directed only to already available pods.
- **Implemented Pre-warming**: Ensured that new pods were ready to handle traffic immediately after scaling.
- **Queue Management**: Introduced logic to the API gateway to manage request queues, ensuring that requests were routed to healthy pods only.
- **Improved Health Checks**: Switched from HTTP-based health checks to TCP checks, reducing false negatives during traffic spikes.

**Result**: 
- The infrastructure stabilized, and requests were distributed more efficiently.
- Pre-warming improved pod readiness, reducing timeouts.
- Health checks became more reliable, leading to fewer pod failures and higher availability (99.9%).

---

### 14. How Do You Prioritize Tasks When Multiple Urgent Issues Arise?

1. **Assess Impact**: Evaluate the severity and impact of each issue and categorize them.
2. **Communicate Transparently**: Keep stakeholders informed about timelines and reasons for prioritization.
3. **Address Critical Tasks First**: Focus on tasks that directly affect service availability or security.
4. **Workarounds or Hotfixes**: Implement quick fixes where possible, while planning for permanent solutions.

