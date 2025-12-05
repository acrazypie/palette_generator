# Palette Generator - Docker Deployment Guide

## Quick Start with Docker

### 1. Start the Application (Production)

```bash
# Using docker-compose (recommended)
docker-compose up -d

# Or using the management script
./docker-manage.sh start
```

The application will be available at: **http://localhost:5000**

### 2. Start the Application (Development)

```bash
# Using docker-compose
docker-compose -f docker-compose.dev.yml up

# Or using the management script
./docker-manage.sh start-dev
```

Development mode includes:

-   Hot reload on file changes
-   Debug toolbar
-   Better error messages

### 3. Management Commands

```bash
# View logs
./docker-manage.sh logs

# Stop the application
./docker-manage.sh stop

# Rebuild the image
./docker-manage.sh rebuild

# Open a shell in the container
./docker-manage.sh shell

# Clean up all Docker resources
./docker-manage.sh clean

# Show help
./docker-manage.sh help
```

## Docker File Descriptions

### `Dockerfile`

Production-ready image with:

-   Minimal base image (python:3.11-slim)
-   Non-root user for security
-   Health checks
-   Optimized layers for caching

### `Dockerfile.dev`

Development image with:

-   Additional debugging tools
-   Flask debug toolbar
-   Hot reload capability
-   Interactive terminal support

### `docker-compose.yml`

Production composition with:

-   Service definition
-   Port mapping (5000:5000)
-   Volume mounts for code
-   Health check configuration
-   Network setup

### `docker-compose.dev.yml`

Development composition with:

-   Full volume mounts for hot reload
-   Interactive terminal
-   Environment variables for debug mode

### `.dockerignore`

Excludes unnecessary files from Docker build:

-   Python cache and virtual environments
-   Git files
-   IDE configurations
-   Documentation

## Configuration

### Environment Variables

Create a `.env` file:

```bash
cp .env.example .env
```

Edit `.env` with your settings:

```
FLASK_ENV=production
FLASK_APP=run.py
FLASK_DEBUG=0
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
```

### Port Configuration

To change the port (e.g., 8000), edit `docker-compose.yml`:

```yaml
ports:
    - "8000:5000" # Host port 8000 → Container port 5000
```

## Common Tasks

### Build the Docker Image

```bash
# Build with the default Dockerfile
docker build -t palette-generator:latest .

# Or use the build script
./build-docker.sh palette-generator latest

# Push to a registry
./build-docker.sh palette-generator latest myregistry.com
```

### View Container Logs

```bash
# Real-time logs
docker logs -f palette_generator

# Or using compose
docker-compose logs -f

# Or using the management script
./docker-manage.sh logs
```

### Execute Commands in Container

```bash
# Open a shell
docker exec -it palette_generator bash

# Run a Python command
docker exec palette_generator python -c "import app; print('OK')"

# Using the management script
./docker-manage.sh shell
```

### Stop and Remove Everything

```bash
# Stop running containers
docker-compose down

# Remove containers, networks, and volumes
docker-compose down -v

# Or use the management script
./docker-manage.sh clean
```

## Production Deployment

### Using Gunicorn

For production, use Gunicorn instead of Flask's development server:

```bash
# Install gunicorn
pip install gunicorn

# Update Dockerfile to use Gunicorn
CMD ["gunicorn", "--config", "wsgi.py", "run:app"]
```

### Docker Registry Push

```bash
# Tag the image
docker tag palette-generator:latest myregistry.com/palette-generator:latest

# Push to registry
docker push myregistry.com/palette-generator:latest

# Pull and run
docker run -p 5000:5000 myregistry.com/palette-generator:latest
```

### Multi-stage Build (Advanced)

For smaller production images, use multi-stage builds in the Dockerfile:

```dockerfile
# Build stage
FROM python:3.11-slim as builder
...

# Runtime stage
FROM python:3.11-slim
COPY --from=builder /app /app
...
```

## Troubleshooting

### Container Fails to Start

Check logs:

```bash
docker logs palette_generator
```

### Port 5000 Already in Use

Change the port in `docker-compose.yml`:

```yaml
ports:
    - "8000:5000"
```

### File Permissions Issues

Rebuild the image:

```bash
docker-compose build --no-cache
```

### Changes Not Reflected (Development)

Restart the container:

```bash
docker-compose restart palette_generator_dev
```

## Performance Tips

1. **Layer Caching**: Dockerfile copies `requirements.txt` first to reuse layers
2. **Image Size**: Uses `python:3.11-slim` (~150MB vs ~900MB for full image)
3. **Multi-stage Builds**: Can reduce production image size further
4. **Health Checks**: Configured to detect container issues early

## Security Best Practices

✅ Non-root user (appuser) runs the application  
✅ Health checks configured  
✅ No hardcoded secrets in Dockerfile  
✅ Environment variables for configuration  
✅ Minimal base image reduces attack surface

## Next Steps

1. Configure environment variables
2. Set up container registry (Docker Hub, ECR, etc.)
3. Implement CI/CD pipeline
4. Set up monitoring and logging
5. Configure backup and restore procedures

For more information, see the main [README.md](README.md)
