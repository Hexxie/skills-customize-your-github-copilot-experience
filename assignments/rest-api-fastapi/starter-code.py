from typing import Dict, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Simple FastAPI Assignment")


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


db: Dict[int, Item] = {}


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment"}


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items/", response_model=Item)
def create_item(item: Item):
    if item.id in db:
        raise HTTPException(status_code=400, detail="Item already exists")
    db[item.id] = item
    return item
