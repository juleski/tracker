from fastapi import Depends, FastAPI, Header, HTTPException
from .routers import items, users
from app.funnels.registration import registration_endpoint
from app.funnels.interactions import interactions_endpoint

app = FastAPI()

async def get_token_header(auth_token: str = Header(...)):
    if auth_token != 'fake-secret-token':
        raise HTTPException(status_code=400, detail='X-token header invcalid')


app.include_router(users.router)
app.include_router(
    items.router,
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"Description": "Not found"}}
)
app.include_router(
    registration_endpoint.router,
    prefix="/registration",
    tags=["registration"]
)
app.include_router(
    interactions_endpoint.router,
    prefix="/interactions",
    tags=["interactions"]
)