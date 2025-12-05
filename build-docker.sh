#!/usr/bin/env bash
# Build and push Docker image to registry (customize as needed)

set -e

IMAGE_NAME="${1:-palette-generator}"
IMAGE_TAG="${2:-latest}"
REGISTRY="${3:-}"

if [ -z "$REGISTRY" ]; then
    FULL_IMAGE_NAME="$IMAGE_NAME:$IMAGE_TAG"
else
    FULL_IMAGE_NAME="$REGISTRY/$IMAGE_NAME:$IMAGE_TAG"
fi

echo "Building Docker image: $FULL_IMAGE_NAME"
docker build -t "$FULL_IMAGE_NAME" .

echo "Build complete!"
echo "To run the image:"
echo "  docker run -p 5000:5000 $FULL_IMAGE_NAME"

if [ ! -z "$REGISTRY" ]; then
    echo ""
    echo "To push to registry:"
    echo "  docker push $FULL_IMAGE_NAME"
fi
