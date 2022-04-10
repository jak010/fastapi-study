# Nested Models


from typing import Optional, Set
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []
    image: Optional[Image] = None


# Request Body Example
"""
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "image" : {
        "url":"http://some-image.com",
        "name":"some-name"
    }
}
"""


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    result = {"item_id": item_id, "item": item}
    return result
