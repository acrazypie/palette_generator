# Docker Setup Guide - Palette Generator

## Overview

This guide covers how to run the Palette Generator application using Docker and Docker Compose.

## Prerequisites

-   Docker >= 20.10
-   Docker Compose >= 1.29
-   Git (for cloning the repository)

## Quick Start

### Production Environment

1. **Clone the repository**

    ```bash
    git clone <repository-url>
    cd palette_generator
    ```

2. **Build and run with Docker Compose**

    ```bash
    docker-compose up -d
    ```

3. **Access the application**

    - Open your browser and navigate to `http://localhost:5000`

4. **Stop the application**
    ```bash
    docker-compose down
    ```

### Development Environment

1. **Run with development configuration**

    ```bash
    docker-compose -f docker-compose.dev.yml up
    ```

2. **Hot reload enabled**

    - The development setup automatically reloads on file changes
    - Access the application at `http://localhost:5000`

3. **Stop the development environment**
    ```bash
    docker-compose -f docker-compose.dev.yml down
    ```

## Common Docker Commands

### View running containers

```bash
docker ps
```

### View container logs

```bash
docker logs palette_generator
```

### Follow logs in real-time

```bash
docker logs -f palette_generator
```

### Execute command in running container

```bash
docker exec -it palette_generator bash
```

### Rebuild the image

```bash
docker-compose build --no-cache
```

### Remove all containers and volumes

```bash
docker-compose down -v
```

## File Structure

```
palette_generator/
├── Dockerfile              # Production image
├── Dockerfile.dev          # Development image with debug tools
├── docker-compose.yml      # Production compose configuration
├── docker-compose.dev.yml  # Development compose configuration
├── .dockerignore          # Files to exclude from Docker build
├── docker-entrypoint.sh   # Entrypoint script
├── .env.example           # Example environment variables
├── requirements.txt       # Python dependencies
├── run.py                 # Flask entry point
├── config.py              # Application configuration
├── app/                   # Main application directory
│   ├── __init__.py
│   ├── palette.py         # Palette generation logic
│   ├── routes.py          # API routes
│   ├── static/            # Static files (CSS, JS)
│   └── templates/         # HTML templates
└── README_DOCKER.md       # This file
```

## Environment Variables

Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

Available environment variables:

-   `FLASK_ENV`: Set to `development` or `production`
-   `FLASK_APP`: Application entry point (default: `run.py`)
-   `FLASK_DEBUG`: Enable debug mode (0 or 1)
-   `FLASK_HOST`: Host to bind to (default: `0.0.0.0`)
-   `FLASK_PORT`: Port to bind to (default: `5000`)

## Health Check

Both production and development configurations include health checks. To manually check:

```bash
curl http://localhost:5000/
```

## Troubleshooting

### Port Already in Use

If port 5000 is already in use, modify the port mapping in `docker-compose.yml`:

```yaml
ports:
    - "8000:5000" # Map port 8000 on host to 5000 in container
```

### Permission Denied

The container runs as a non-root user (`appuser`) for security. If you need root access:

```bash
docker exec -it --user root palette_generator bash
```

### Container Won't Start

Check logs for errors:

```bash
docker logs palette_generator
```

### Rebuild Without Cache

If changes aren't reflected:

```bash
docker-compose build --no-cache
docker-compose up -d
```

## Performance Optimization

### Reduce Image Size

The Dockerfile uses `python:3.11-slim` to minimize image size. Current image size: ~200MB

### Layer Caching

The Dockerfile copies `requirements.txt` first to leverage Docker's layer caching. Dependencies are only reinstalled if `requirements.txt` changes.

## Security Notes

-   Application runs as non-root user (`appuser`)
-   No sensitive data in environment variables (use `.env` for secrets)
-   Regular security updates for base image (`python:3.11-slim`)
-   Health checks configured to detect issues early

## Next Steps

-   Configure environment variables in `.env`
-   Customize port mappings as needed
-   Set up proper logging and monitoring
-   Implement CI/CD pipeline with Docker

## Support

For issues or questions, refer to:

-   [Docker Documentation](https://docs.docker.com/)
-   [Docker Compose Documentation](https://docs.docker.com/compose/)
-   [Flask Documentation](https://flask.palletsprojects.com/)
