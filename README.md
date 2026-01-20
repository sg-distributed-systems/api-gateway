# api-gateway

Entry point that receives requests and routes them to backend services.

## Why this repo exists

The API gateway provides a single entry point for all client requests, handling routing, request validation, and traffic management before forwarding to downstream services.

## Core Components

### `handle_request(path: str)`
Processes an incoming request and routes it to the appropriate backend service.

**Logs:**
- `request_received` — Logged when a new request arrives, includes the request path
- `request_routed` — Logged after determining the destination service

### `load_config(service_name: str) -> ServiceConfig`
Loads service configuration from environment variables including `APP_ENV` and `SHUTDOWN_TIMEOUT_SECONDS`.

### `AppError`
Base exception class for application errors. Provides `to_log_fields()` for structured error logging.

### `install_signal_handlers(service_logger_name: str)`
Installs SIGINT/SIGTERM handlers for graceful shutdown with logging.

### `init_correlation_id() -> str`
Initializes a correlation ID from the `CORRELATION_ID` environment variable or generates a UUID4.

## HTTP Interface

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/healthz` | GET | Liveness probe |
| `/readyz` | GET | Readiness probe |
| `/gateway/handle` | POST | Handles and routes a request |

### Running the service

```bash
uvicorn src.api_gateway.app:app --host 0.0.0.0 --port 8000
```
