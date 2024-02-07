# Sample Time App

This repository contains a simple Flask application that returns the current server time. The application is containerized using Docker, making it easy to deploy to Kubernetes.

## Application Details

- **Language**: Python 3
- **Framework**: Flask
- **Docker Base Image**: python:3.5

## Getting Started

These instructions will cover usage information and for the docker container

### Prerequisities

In order to run this container you'll need [docker](https://docs.docker.com/mac/started/) installed.

### Usage

#### Building the Image

To build the image from the Dockerfile:

```shell
docker build -t USERNAME/sample-timeapp:latest .
```

Replace `USERNAME` with your Docker Hub username.

Run the image from the Docker registry:

```shell
docker run --name sample-time-app -p 8080:8080 -d USERNAME/sample-timeapp:latest
```

Visit `http://localhost:8080/time` to view the current time.

#### Environment Variables

- `PORT` - The port the server listens to (default `8080`)

### Kubernetes Deployment

To deploy this application to a Kubernetes cluster, use the following commands:

```shell
kubectl create deployment sample-time-app --image=docker.io/USERNAME/sample-timeapp:latest
kubectl expose deployment sample-time-app --type="NodePort" --port 8080
```

Check the deployment and service:

```shell
kubectl get deployments
kubectl get services
```

Access the application via `http://<IP>:<NodePort>`.
