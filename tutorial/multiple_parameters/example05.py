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

# Embed a single body parameter¶
# - 받는 키 값을 내장 시켜버리기


app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item = Body(..., embed=True)):  # -  왜 안되지?
    results = {"item_id": item_id, "item": item}
    return results
