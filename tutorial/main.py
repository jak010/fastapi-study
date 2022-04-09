"""Note

 >> fastapi 서버 실행하기

   $ uvicorn main:app --reload
   1. main은 파일명을 가리킴


"""

from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
