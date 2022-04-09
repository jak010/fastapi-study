from typing import Optional
from fastapi import FastAPI, Form

from pydantic import BaseModel

app = FastAPI()


# 이 구조는 raw json을 통해 보낼 수 있음

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post("/items")
def create_item(item: Item):
    print(item.name.capitalize())
    return item
