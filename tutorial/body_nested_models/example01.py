# Body Nested Models


from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List = [] # Nested Field


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
