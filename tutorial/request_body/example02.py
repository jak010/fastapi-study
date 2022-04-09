from typing import Optional
from fastapi import FastAPI, Form

from pydantic import BaseModel

app = FastAPI()


# 이 구조는 multipart-form 으로 보낼 수 있음

@app.post("/items")
def create_item(
        name: str = Form(...),
        description: Optional[str] = Form(...),
        price: float = Form(...),
        tax: Optional[float] = Form(...)
):
    items = {}
    items.update({"name": name})
    items.update({"description": description})
    items.update({"price": price})
    items.update({"tax": tax})
    return items
