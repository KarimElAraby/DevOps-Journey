# DevOps Journey

![WhatsApp Image 2024-06-01 at 1 25 16 AM](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/978a1c14-cfaa-49b4-97e9-22ae0385b754)


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

   ![Screenshot from 2024-04-17 00-14-59](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/4b8742d4-1eb6-407d-a4f3-30ce6fc00693)


2. **Install Nginx Ingress Controller:**

    ```sh
    kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
    ```

3. **Verify the Nginx Ingress Controller:**

    ```sh
    kubectl get pods -n ingress-nginx
    ```
![Screenshot from 2024-05-31 21-06-28](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/6e4d2517-d0c6-4ce3-bb87-b7dfb064899f)

4. **Install ArgoCD:**

    ```sh
    kubectl create namespace argocd
    kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
    ```

5. **Access ArgoCD UI:**

    Forward the ArgoCD server port to localhost:

    ```sh
    kubectl port-forward svc/argocd-server -n argocd 8080
    ```

    Access the ArgoCD UI at `https://localhost:8080`.

![Screenshot from 2024-05-30 03-28-46](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/f07e7452-fdee-4423-8c5a-81e7e9933905)
![Screenshot from 2024-05-30 03-31-31](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/671d65ee-5f95-4bc3-b7a3-cf43e1372a32)
![Screenshot from 2024-05-30 03-31-42](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/41332b1b-cf1e-40ce-a588-fae010d4ce53)

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
![Screenshot from 2024-05-29 03-29-44](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/3c70a778-c733-4b5c-8093-15e4296bbc79)

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
![Screenshot from 2024-05-31 21-19-02](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/a24c6980-f4eb-4b56-aab8-249d234a2630)
![Screenshot from 2024-05-31 21-19-28](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/6a2453a7-291c-4f1f-aaf7-c45df907926d)

4. **Configure Jenkins:**

    - Install necessary plugins (e.g., Kubernetes, Git, ArgoCD).
    - Create a pipeline job with the following stages:
      - Build
      - Test
      - Deploy
![Screenshot from 2024-05-29 02-59-13](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/e17dd448-fb1b-49a1-9c3c-535b3ca69bf0)

![Screenshot from 2024-05-31 21-22-07](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/5fc091dd-bf1f-45ef-81bd-05714cb6c66b)

![Screenshot from 2024-06-02 01-35-24](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/cfc0cabb-af8f-49bb-a285-8eecde4e3585)

![Screenshot from 2024-06-02 01-35-35](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/c807c986-2eb9-4d2c-b138-2d7fafb9e689)

![Screenshot from 2024-06-02 01-35-43](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/4eecbe4c-08b1-461b-873e-a3d46032607a)

![Screenshot from 2024-06-02 01-35-47](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/4e51473d-c8f6-4ffa-8da5-e9db1de8668b)


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

   ![Screenshot from 2024-06-01 18-02-12](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/5e825e40-ad34-4f96-8177-b343806cf7cd)

## Monitoring with Prometheus and Grafana

### Prometheus

Prometheus is configured to scrape metrics from your application and Kubernetes components.
![Screenshot from 2024-05-29 03-14-52](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/ae4c6a36-160e-474b-95fb-84a6c2f227e3)
![Screenshot from 2024-05-30 02-33-10](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/41c7333b-8170-4766-af17-727d01443a40)

### Grafana

Grafana is used to visualize the metrics collected by Prometheus. Pre-configured dashboards can be imported to monitor application health, performance, and resource usage.
![Screenshot from 2024-05-30 02-19-22](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/26e5ff42-a58b-42c2-ab74-b204a0f08fe9)
![Screenshot from 2024-05-30 02-19-53](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/90aaf39a-9bd1-4ba8-b0ab-91fe6ba3e12b)

### GitOps - CD with ArgoCD


    ```sh
    kubectl apply -f manifests/application.yaml
    ```

Access the ArgoCD UI at https://localhost:8080.
![Screenshot from 2024-06-02 01-26-17](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/b3ac0180-3f64-42c2-9a2f-97661fa42e33)

![Screenshot from 2024-06-02 01-25-46](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/8f1ec23d-c1aa-4f20-96e5-85c6e9975cfe)

![Screenshot from 2024-06-02 01-25-57](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/436d3a52-006a-4e92-8a90-a851b4c0893a)

![Screenshot from 2024-06-02 01-26-07](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/ca9240cc-c62e-4a2b-afab-948aa35c4bcf)

![Screenshot from 2024-06-02 01-35-47](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/560baa1d-a1f0-4051-bbc5-a35973d832c4)

![Screenshot from 2024-06-02 01-28-03](https://github.com/KarimElAraby/DevOps-Journey/assets/137705973/b6aa2057-86f2-4c00-83f4-729996b6b15c)


