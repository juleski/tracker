from fastapi import APIRouter, Depends, Header, HTTPException
from pydantic import BaseModel
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class User(BaseModel):
    name: str
    email: str
    price: float
    amount: int
    description: str = None


router = APIRouter()


async def verify_token(auth_token: str = Header(...)):
    if auth_token != "fake-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


@router.get("/users/", tags=["users"], dependencies=[Depends(verify_token)])
async def read_uses(page_num: int = 1, page_size: int = 20, is_num: bool = None):
    print(type(is_num), is_num)
    return [{"username": "Foo"}, {"username": "Bar"}]

@router.get("/users/{username}", tags=["users"])
async def read_user(username: int):
    return {"username": username}


@router.post("/users/", tags=["users"])
async def create_user(user: User):
    return user


@router.get("/test/{model_name}", tags=["test"])
async def read_test(model_name: ModelName):
    return {"model_name": model_name.value}


@router.get("/files/{file_path:path}", tags=["files"])
async def read_file(file_path: str):
    return {"file_path": file_path}