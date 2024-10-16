from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/items/{item_id}")
async def get_item(item_id: str):
    return {"item_id": item_id}


@app.get("/users/me")
async def get_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet: # different ways to compare
        return {"model_name": model_name,
                "message": "Deep Learning FTW!"}
    
    if model_name.value == "lenet": # different ways to compare
        return {"model_name": model_name,
                "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}
