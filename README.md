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
