# DevOps Journey

## Overview

This project demonstrates the deployment of a 3-tier application (frontend, backend, and SQL database) on a Kubernetes cluster using `kind` (Kubernetes IN Docker). The application is exposed externally via an Nginx ingress controller and features a robust CI/CD pipeline configured with Jenkins and ArgoCD. Additionally, the setup includes monitoring using Prometheus and Grafana.

## Table of Contents

- [Overview](#overview)
- [Setup Instructions for KinD Cluster](#setup-instructions-for-kind-cluster)
- [CI/CD Pipeline Configuration](#cicd-pipeline-configuration)
- [Kubernetes Manifests and Application Architecture](#kubernetes-manifests-and-application-architecture)
- [Monitoring with Prometheus and Grafana](#monitoring-with-prometheus-and-grafana)
- [GitOps - CD with ArgoCD](#gitops---cd-with-argocd)

## Setup Instructions for KinD Cluster

### Prerequisites

- Docker installed on your machine
- `kubectl` command-line tool installed
- `kind` tool installed

### Setting Up the KinD Cluster

1. **Create a KinD cluster:**

    ```sh
    kind create cluster --config manifests-k8s/cluster_config --name my-cluster
    ```

    ![KinD Cluster Creation](path/to/screenshot.png)

2. **Install Nginx Ingress Controller:**

    ```sh
    kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
    ```

3. **Verify the Nginx Ingress Controller:**

    ```sh
    kubectl get pods -n ingress-nginx
    ```

    ![Nginx Ingress Controller Pods](path/to/screenshot.png)

4. **Install ArgoCD:**

    ```sh
    kubectl create namespace argocd
    kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
    ```

5. **Access ArgoCD UI:**

    Forward the ArgoCD server port to localhost:

    ```sh
    kubectl port-forward svc/argocd-server -n argocd 8080:443
    ```

    Access the ArgoCD UI at `https://localhost:8080`.

    ![ArgoCD UI](path/to/screenshot.png)

6. **Install Prometheus and Grafana:**

    Use Helm to install Prometheus and Grafana:

    ```sh
    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm repo update
    helm install prometheus prometheus-community/prometheus
    helm install grafana grafana/grafana
    ```

    Access Grafana UI by port forwarding:

    ```sh
    kubectl port-forward svc/grafana 3000
    ```

    Default credentials for Grafana are `admin/admin`.

    ![Grafana UI](path/to/screenshot.png)

## CI/CD Pipeline Configuration

### Jenkins Setup

1. **Deploy Jenkins:**

    ```sh
    kubectl apply -f manifests-k8s/jenkins/deployment.yaml
    ```

2. **Expose Jenkins using NodePort:**

    Apply the service configuration:

    ```sh
    kubectl apply -f manifests-k8s/jenkins/service.yaml
    ```

3. **Access Jenkins:**

    Find the IP of your `kind` node and access Jenkins at `http://<node-ip>:32000`.

    ![Jenkins UI](path/to/screenshot.png)

4. **Configure Jenkins:**

    - Install necessary plugins (e.g., Kubernetes, Git, ArgoCD).
    - Create a pipeline job with the following stages:
      - Build
      - Test
      - Deploy

    ![Jenkins Pipeline](path/to/screenshot.png)

## Kubernetes Manifests and Application Architecture

### Application Architecture

The application consists of three tiers:

1. **Frontend:**
   - Exposed via Nginx ingress
   - Communicates with the backend

2. **Backend:**
   - Handles business logic
   - Communicates with the SQL database

3. **SQL Database:**
   - Stores application data

## Monitoring with Prometheus and Grafana

### Prometheus

Prometheus is configured to scrape metrics from your application and Kubernetes components. You can customize your `prometheus.yaml` configuration to include specific metrics.

### Grafana

Grafana is used to visualize the metrics collected by Prometheus. Pre-configured dashboards can be imported to monitor application health, performance, and resource usage.

### Access Grafana

Port forward the Grafana service to access the UI:

```sh
kubectl port-forward svc/grafana 3000:80
```
Default credentials are admin/admin.


### GitOps - CD with ArgoCD

Access the ArgoCD UI at https://localhost:8080.