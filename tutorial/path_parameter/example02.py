from enum import Enum

from fastapi import FastAPI

app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    print(model_name)

    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": " alexnet"}

    if model_name == ModelName.resnet:
        return {"model_name": model_name, "message": " resnet"}
