from typing import Dict, List
from pydantic import BaseModel, Field

class hue_dict(BaseModel):
    id: str = Field(..., description="hub id")
    internalipaddress: str = Field(..., description="Your hubs IP Address")
    port: int = Field(..., description="The port your hub listens on")

class hue_response(BaseModel):
    response: List[hue_dict]