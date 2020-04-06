from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/")
async def read_items():
    return [{"name": "Item foo"}, {"name": "Item bar"}]


@router.get("/{item_id}", responses={401: {"description": "awtsu"}})
async def read_item(item_id: str):
    if item_id != "aw":
        raise HTTPException(status_code=401, detail="item shizntis")
    return {"name": "Fake Specific Item", "item_id": item_id}


@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "foo":
        raise HTTPException(status_code=403, detail="You can only update the item: foo")
    return {"item_id": item_id, "name": "The Fighters"}