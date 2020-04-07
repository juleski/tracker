from fastapi import APIRouter, Body
from pydantic import BaseModel

router = APIRouter()

class Device(BaseModel):
    device_id: str


@router.post("/")
async def register_user(
    *,
    device_id: str = Body(..., embed=True, title="Unique id of device")
):
    return {'device_id': device_id}