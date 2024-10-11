from fastapi import FastAPI

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