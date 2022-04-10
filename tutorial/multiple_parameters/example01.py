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


# request body, path, body 를 한 번에 사용하는 방법
@app.put("/items/{item_id}")
def update_itme(
        *,
        item_id: int = Path(..., title="THe Id of the itme to get", ge=0, le=1000),  # path
        q: Optional[str] = None,  # query
        item: Optional[Item] = None,  # body
):
    results = {'item_id': item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})

    return results
