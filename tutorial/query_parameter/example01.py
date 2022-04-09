from typing import Optional

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz2"},
    {"item_name": "Baz3"},
    {"item_name": "Baz4"},
    {"item_name": "Baz5"},
]


# http://127.0.0.1:8000/items/?skip=0&limit=10
# 경로 매개 변수가 아닌 경우 "쿼리" 매개 변수로 자동 해석함
@app.get("/items/")
def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


# 선택적 매개변수
# -- 경로 매개 변수와 쿼리 매개 변수를 같이 사용할 경우는?
# A. 구분은 잘 된다
@app.get("/items2/{item_id}")
def read_item2(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
