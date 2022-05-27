from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel






class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


app = FastAPI()

inventory = {
             # 1 : {
             #     "name": "Milk",
             #     "price" : 3.97,
             #     "brand" : "Regular"
             # },
             #
             # 2: {"name": "Water",
             #     "price" : 2.5,
             #     "brand" : "Cristalline"
             #     }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="DONNE UN ID")):
    return inventory[item_id]

@app.get("/get-by-name/{item_id}")
def get_item(*, item_id: int, test: int, name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail = "Item name not found")


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return{"Error" : "ItemID already exists."}

    inventory[item_id] = item
    return inventory


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):

    if item_id not in inventory:
        return{"Error" : "ItemID not in inventory"}

    if item.name != None:
        inventory[item_id].name = item.name

    if item.price != None:
        inventory[item_id].price = item.price

    if item.brand != None:
        inventory[item_id].brand = item.brand

    return inventory


@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description = "The ID of the item to delete", gt=0)):
    if item_id not in inventory:
        return{"Error" : "ItemID not in inventory"}
    del inventory[item_id]
    return inventory








#%%
