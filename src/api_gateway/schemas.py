"""
Pydantic models for API request and response validation.

Defines data transfer objects used for request parsing and response
serialization in the API layer.
"""
from typing import Dict, Optional

from pydantic import BaseModel, Field


class HandleRequestRequest(BaseModel):
    path: str
    method: str
    headers: Dict[str, str] = Field(default_factory=dict)
    body: Optional[str] = None


class HandleRequestResponse(BaseModel):
    status_code: int
    latency_ms: float
    routed_to: str
