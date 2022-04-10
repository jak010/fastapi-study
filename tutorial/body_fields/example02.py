"""Note

 >> fastapi 서버 실행하기

   $ uvicorn main:app --reload

   1. main은 파일명을 가리킴
   2. app 은 FastAPI() 라인에서 생성한 object
   3. --reload : 코드 변경 후 서버 재시작 (개발시에만 사용할 것)


"""

from typing import Optional
from fastapi import FastAPI, Path, Body
from pydantic import BaseModel, Field

app = FastAPI()


# Declare model attributes
class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        None,
        title="The description of the item",
        description="The description of the item des",
        max_length=300
    )
    price: float = Field(..., gt=0, description="The price Must be greator than zero")
    tax: Optional[float] = None


@app.put("/items/{item_id}")
def update_itme(
        item_id: int,
        item: Item = Body(..., embed=True)
):
    results = {'item': item, 'item_id': item_id}
    return results
