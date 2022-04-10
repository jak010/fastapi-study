# Deeply Nested Models
from typing import List, Optional, Set

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    images: Optional[List[Image]] = None


class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]


"""Request Body
{
    "name": "string",
    "description": "string",
    "price": 0,
    "items": [
        {
            "name": "string",
            "description": "string",
            "price": 0,
            "tax": 0,
            "tags": [],
            "images": [
                {
                    "url": "http://www.naver.com",
                    "name": "string"
                }
            ]
        }
    ]
}
"""


@app.post("/offers/")
def create_offer(offer: Offer):
    return offer
