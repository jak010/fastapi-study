# Body Nested Models


from typing import Optional, List, Set
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    #  필드 원소가 중복값이라면 set으로 중복을 제거할 수 있음
    # - 근데 순서가 이상해짐
    tags: Set[str] = set()

    # 아래와 같은 방식으로 정렬도 가능함
    # tags: Set[str] = sorted(set())


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
