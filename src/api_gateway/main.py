from core_logger import get_logger

logger = get_logger("api-gateway")


def handle_request(path: str) -> None:
    logger.info("request_received", path=path)
    logger.debug("request_routed", path=path, destination="backend")


def main() -> None:
    handle_request("/users/123")


if __name__ == "__main__":
    main()
