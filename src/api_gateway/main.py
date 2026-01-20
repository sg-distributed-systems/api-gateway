"""
Service entrypoint for the api-gateway.

This module serves as the application entry point, responsible solely for
initializing and running the uvicorn ASGI server. All business logic is
contained in service.py; this file handles only server configuration and startup.

Usage:
    python -m api_gateway.main
"""
import uvicorn

from api_gateway.app import app
from api_gateway.config import load_config


def main() -> None:
    cfg = load_config("api-gateway")
    uvicorn.run(app, host="0.0.0.0", port=cfg.port)


if __name__ == "__main__":
    main()
