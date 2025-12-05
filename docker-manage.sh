#!/usr/bin/env bash
# Helper script to manage the application with Docker

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

function print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

function print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

function print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

function print_usage() {
    cat << EOF
Usage: $0 <command> [options]

Commands:
    start           Start the application (production)
    start-dev       Start the application (development)
    stop            Stop the application
    logs            Show application logs
    logs-dev        Show development logs
    build           Build the Docker image
    rebuild         Rebuild the Docker image without cache
    clean           Remove containers and volumes
    shell           Open a shell in the running container
    test            Run tests in the container
    help            Show this help message

Examples:
    $0 start           # Start production environment
    $0 start-dev       # Start development environment
    $0 logs            # View production logs
    $0 stop            # Stop the application
    $0 clean           # Clean up Docker resources

EOF
}

case "$1" in
    start)
        print_info "Starting Palette Generator (Production)..."
        docker-compose up -d
        print_info "Application is running on http://localhost:5000"
        ;;
    start-dev)
        print_info "Starting Palette Generator (Development)..."
        docker-compose -f docker-compose.dev.yml up
        ;;
    stop)
        print_info "Stopping Palette Generator..."
        docker-compose down
        print_info "Application stopped"
        ;;
    logs)
        docker-compose logs -f
        ;;
    logs-dev)
        docker-compose -f docker-compose.dev.yml logs -f
        ;;
    build)
        print_info "Building Docker image..."
        docker-compose build
        print_info "Build complete"
        ;;
    rebuild)
        print_info "Rebuilding Docker image (no cache)..."
        docker-compose build --no-cache
        print_info "Build complete"
        ;;
    clean)
        print_warning "This will remove all containers and volumes"
        read -p "Are you sure? (y/N) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            print_info "Cleaning up..."
            docker-compose down -v
            print_info "Cleanup complete"
        fi
        ;;
    shell)
        print_info "Opening shell in running container..."
        docker exec -it palette_generator bash
        ;;
    test)
        print_info "Running tests..."
        docker-compose exec palette-generator python -m pytest
        ;;
    help|--help|-h)
        print_usage
        ;;
    *)
        print_error "Unknown command: $1"
        echo ""
        print_usage
        exit 1
        ;;
esac
