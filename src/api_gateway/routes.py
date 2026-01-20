"""
API route definitions for the service.

Defines FastAPI router endpoints that handle incoming HTTP requests and
delegate to core business logic functions.
"""
from fastapi import APIRouter

from .schemas import HandleRequestRequest, HandleRequestResponse
from .service import handle_request

router = APIRouter()


@router.post("/gateway/handle", response_model=HandleRequestResponse, status_code=200)
def handle_request_route(req: HandleRequestRequest) -> HandleRequestResponse:
    result = handle_request(
        path=req.path,
        method=req.method,
        headers=req.headers,
        body=req.body,
    )
    return HandleRequestResponse(
        status_code=result["status_code"],
        latency_ms=result["latency_ms"],
        routed_to=result["routed_to"],
    )
