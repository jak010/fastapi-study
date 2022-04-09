from typing import Optional

from fastapi import FastAPI

app = FastAPI()


# 쿼리 매개변수 형변환
@app.get("/items/{item_id}")
def read_item2(item_id: str,
               q: Optional[str] = None,
               short: bool = False
               ):
    # short
    # true, false
    # on, off
    # 0,1

    items = {"item_id": item_id}

    if q:
        items.update({"item_id": item_id, "q": q})

    items.update({"short": short})

    return items
