"""Note

 >> fastapi 서버 실행하기

   $ uvicorn main:app --reload

   1. main은 파일명을 가리킴
   2. app 은 FastAPI() 라인에서 생성한 object
   3. --reload : 코드 변경 후 서버 재시작 (개발시에만 사용할 것)


"""

from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


#  Singular values in body
# - 모델 선언 방식 외에 추가로 request body에 value를 받는 방법
@app.put("/items/{item_id}")
def update_itme(
        item_id: int,
        item: Item,
        user: User,
        importance: int = Body(...)
):
    results = {'item_id': item_id, "item": item, "user": user, "importance": importance}

    return results
