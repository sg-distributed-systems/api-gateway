from fastapi import APIRouter

from .main import handle_request
from .schemas import HandleRequestRequest, HandleRequestResponse

router = APIRouter()


@router.post("/gateway/handle", response_model=HandleRequestResponse)
def handle_request_route(req: HandleRequestRequest) -> HandleRequestResponse:
    handle_request(req.path)
    return HandleRequestResponse(status="ok")
