"""
Service entrypoint with lifecycle management.

Initializes configuration, correlation ID, and signal handlers before running
the main service logic. Provides structured error handling for all exceptions.
"""
from core_logger import get_logger

from api_gateway.config import load_config
from api_gateway.errors import AppError
from api_gateway.lifecycle import install_signal_handlers
from api_gateway.observability import init_correlation_id

logger = get_logger("api-gateway")


def handle_request(path: str) -> None:
    logger.info("request_received", path=path)
    logger.debug("request_routed", path=path, destination="backend")


def run() -> None:
    cfg = load_config("api-gateway")
    cid = init_correlation_id()
    install_signal_handlers("api-gateway")

    logger.info("service_starting", env=cfg.env, correlation_id=cid)

    try:
        handle_request("/users/123")
        logger.info("service_completed")
    except AppError as e:
        logger.warning("app_error", **e.to_log_fields())
        raise
    except Exception as e:
        logger.exception("unhandled_exception", exc=e)
        raise


def main() -> None:
    run()


if __name__ == "__main__":
    main()
