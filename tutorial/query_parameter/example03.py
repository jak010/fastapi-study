from typing import Optional

from fastapi import FastAPI

app = FastAPI()


# mutliple path/query parameter
# 매개변수로 넘길 경우 순서를 기억하기 떄문에 url 순서를 굳이 맞출 필요는 없음
@app.get("/users/{user_id}/items/{item_id}")
def read_item2(item_id: str,
               user_id: int,
               q: Optional[str] = None,
               short: bool = False
               ):
    items = {}

    items.update({"item_id": item_id})
    items.update({"user_id": user_id})
    items.update({"q": q})
    items.update({"short": short})

    return items


# Required Parameter
# 쿼리 파라미터에 기본값을 안 주면 됨
@app.get("/items/{item_id}")
def read_item_id(item_id: int, needy: str = None):
    items = {}
    items.update({"item_id": item_id})
    items.update({"needy": needy})

    return items
