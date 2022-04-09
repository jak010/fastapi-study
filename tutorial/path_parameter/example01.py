"""Note
 >> Path Parameter
"""

from typing import Optional, List
from fastapi import FastAPI

app = FastAPI()


# @app.get("/items/{item_id}")
# def read_item_id_string(item_id):
#     # 이 함수는 item_id에 대해 string으로 동작함
#     return {
#         "item_id": item_id
#     }
#
#
@app.get("/items/{item_id}")
def read_item_id_int(item_id: int):
    # 이 함수는 item_id에 대해 int로 동작함
    return {
        "item_id": item_id
    }

# 이 함수는 에러가 남
# - Path Paramter를 list로 사용하는 일이 없긴 함
# - AssertionError: Path params must be of one of the supported types
# @app.get("/items/{item_id}")
# def read_item_id_int(item_id: List[int]):
#     # 이 함수는 item_id에 대해 int로 동작함
#     return {
#         "item_id": item_id
#     }


""" History
1. 똑같은 경로가 있을 때는 먼저 선언된 경로를 기준으로 잡히는 것 같음

"""
