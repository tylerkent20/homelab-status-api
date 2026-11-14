# Homelab Status API

A containerized Python Flask API deployed on Ubuntu Server.

## Technologies

- Python 3.12
- Flask
- Gunicorn
- Docker
- Docker Compose
- Uptime Kuma

## API Endpoints

- '/' - Application information
- '/health' - Application health
- '/api/status' - Application uptime and status

## Deployment 

docker compose up -d --build

## Monitoring

Uptime Kuma monitors the '/health' endpoint.
