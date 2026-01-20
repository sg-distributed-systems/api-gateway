"""
API route definitions for the service.

Defines FastAPI router endpoints that handle incoming HTTP requests and
delegate to core business logic functions.
"""
from fastapi import APIRouter

from .main import handle_request
from .schemas import HandleRequestRequest, HandleRequestResponse

router = APIRouter()


@router.post("/gateway/handle", response_model=HandleRequestResponse)
def handle_request_route(req: HandleRequestRequest) -> HandleRequestResponse:
    handle_request(req.path)
    return HandleRequestResponse(status="ok")
