"""Note

 >> fastapi 서버 실행하기

   $ uvicorn main:app --reload

   1. main은 파일명을 가리킴
   2. app 은 FastAPI() 라인에서 생성한 object
   3. --reload : 코드 변경 후 서버 재시작 (개발시에만 사용할 것)


"""

from typing import Optional
from fastapi import FastAPI, Path
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


#  Multiple Body Parameter로 전달받아서 처리하기
@app.put("/items/{item_id}")
def update_itme(
        item_id: int,
        item: Item,
        user: User
):
    results = {'item_id': item_id, "item": item, "user": user}

    return results
