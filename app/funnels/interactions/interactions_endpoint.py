from fastapi import APIRouter, Body
from pydantic import BaseModel, Field

router = APIRouter()

class Location(BaseModel):
    lat: float = Field(..., title="Latitude")
    lng: float = Field(..., title="longitude")

@router.post("/")
async def record_interaction(
    *,
    host_device: str = Body(..., embed=True),
    interacted_device: str = Body(..., embed=True),
    location: Location
):
    return {
        "host_device": host_device,
        "interacted_device": interacted_device,
        "location": location
    }