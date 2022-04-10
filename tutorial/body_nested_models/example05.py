# Attributes with lists of submodels¶


from typing import Optional, Set, List
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl  # url이 http 타입이 아니면 에러남
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []
    image: Optional[List[Image]] = None  # Sub Model을 타입으로 지정할 수 있음


# Request Body Example
"""
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "image" : [
    {
        "url":"http://some-image.com",
        "name":"some-name"
    }]
}
"""


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    result = {"item_id": item_id, "item": item}
    return result
