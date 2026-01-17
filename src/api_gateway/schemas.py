from pydantic import BaseModel


class HandleRequestRequest(BaseModel):
    path: str


class HandleRequestResponse(BaseModel):
    status: str
