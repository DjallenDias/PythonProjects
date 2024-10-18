from tkinter.messagebox import showerror
from fastapi import FastAPI
from matplotlib.pyplot import show

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


## DEFAULT VALUES ## 

# Usage - /items1/?skip=0&limit=3
@app.get("/items1/")
async def read_item1(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


##       OPTIONAL PARAMETERS       ##
## CONVERTING QUERY PARAMETER TYPES##

# Usage - /items2/foo?q=3&short=True
# Or -  /items2/foo?q=3
# Or - /items2/foo
# Because q and short are optional
@app.get("/items2/{item_id}")
async def read_item2(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}

    if q:
        item.update({"q": q})
    
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    
    return item


## MULTIPLE ROUTE AND QUERY PARAMETERS ##
@app.get("/users1/{user_id}/items/{item_id}")
async def read_user1_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}    

    if q:
        item.update({"q": q})

    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )

    return item


## MANDATORY QUERY PARAMETERS ##
# Example - /items4/foo-item?needy=sooneedy
@app.get("/items3/{item_id}")
async def read_user_item3(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

# Example - /items4/foo-item?needy=sooneedy&limit=100
@app.get("/items4/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item