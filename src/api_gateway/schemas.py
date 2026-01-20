"""
Pydantic models for API request and response validation.

Defines data transfer objects used for request parsing and response
serialization in the API layer.
"""
from pydantic import BaseModel


class HandleRequestRequest(BaseModel):
    path: str


class HandleRequestResponse(BaseModel):
    status: str
