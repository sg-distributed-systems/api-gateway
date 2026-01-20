"""
Request routing and gateway logic.

Routes incoming HTTP requests to appropriate backend services based on path
matching. Handles request validation, service discovery, and latency tracking
for observability.
"""
import time
from typing import Optional

from core_logger import get_logger

from .errors import NotFoundError, ValidationError

logger = get_logger("api-gateway")

ROUTE_MAP = {
    "/users": "user-service",
    "/orders": "order-service",
    "/payments": "payment-service",
    "/auth": "auth-service",
    "/search": "search-service",
}


def handle_request(
    path: str, method: str, headers: dict, body: Optional[str]
) -> dict:
    start_time = time.monotonic()
    logger.info("request_received", path=path, method=method)

    if method not in {"GET", "POST", "PUT", "DELETE", "PATCH"}:
        raise ValidationError("unsupported_http_method", details={"method": method})

    destination = None
    for prefix, service in ROUTE_MAP.items():
        if path.startswith(prefix):
            destination = service
            break

    if not destination:
        logger.warning("route_not_found", path=path)
        raise NotFoundError("no_matching_route", details={"path": path})

    logger.debug("request_routed", path=path, destination=destination)

    latency_ms = (time.monotonic() - start_time) * 1000
    logger.info("request_completed", path=path, destination=destination, latency_ms=latency_ms)
    return {"status_code": 200, "latency_ms": round(latency_ms, 2), "routed_to": destination}
