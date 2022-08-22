from fastapi import FastAPI, Response, status, HTTPException, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.item import Item
from app.transaction import Transaction

# creating app as instance of FastAPI
app = FastAPI()


# pydantic schema for coin for / PUT request
class Coin(BaseModel):
    coin: int


# function for accessing item quantities as array
def get_quantities():
    quantities = []
    for item in inventory:
        quantities.append(item.get_quantity())
    return quantities


# function for getting the item quantity for a single item
def get_item_quantity(id: int):
    for item in inventory:
        if item._id == id:
            return item


# function for incrementing coin count
def increment_coins(inserted_coin: Coin):
    transaction.set_coin_count(
        transaction.get_coin_count() + inserted_coin.coin)


# dispense item removes two coins from the coin count and returns a value for vended item
def dispense_item(item):
    transaction.set_coin_count(transaction.get_coin_count() - 2)
    item_vended = 1
    item.set_quantity(item.get_quantity() - item_vended)
    return item_vended


# PUT request to add coin
@app.put("/", status_code=status.HTTP_204_NO_CONTENT)
def add_coin(inserted_coin: Coin, response: Response):
    increment_coins(inserted_coin)
    response.headers["X-Coins"] = f"{transaction.get_coin_count()}"


# DELETE request to return coins
@app.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def return_coins(response: Response):
    response.headers["X-Coins"] = f"{transaction.get_coin_count()}"
    transaction.clear_coin_count()


# GET request for global inventory in vending machine
@app.get("/inventory")
def get_machine_inventory():
    quantities = get_quantities()
    return quantities


# GET request for individual item inventory
@app.get("/inventory/{id}")
def get_item_inventory(id: int):
    item = get_item_quantity(id)
    return item.get_quantity()


# PUT request for vending item, returns status code and updates header if can't vend items
@app.put("/inventory/{id}")
def vend_item(id: int, response: Response):
    # checking coin count prior to inventory as coin count won't require querying data source for inventory
    # if held seperately like in a database
    # could reverse order if differently priced items were added to machine at later date
    if transaction.test_coin_count():
        if inventory[id].test_quantity():
            vended_item_quantity = dispense_item(inventory[id])
            response.headers["X-Coins"] = f"{transaction.get_coin_count()}"
            transaction.clear_coin_count()
            return {"Quantity": f"{vended_item_quantity}"}
        else:
            response.headers["X-Coins"] = f"{transaction.get_coin_count()}"
            response.status_code = status.HTTP_404_NOT_FOUND
    else:
        response.headers["X-Coins"] = f"{transaction.get_coin_count()}"
        response.status_code = status.HTTP_403_FORBIDDEN


# instatiating 3 items to add to machine
inventory = []
for i in range(3):
    item = Item(i)
    inventory.append(item)

# creating transaction with coin count of 0 for machine on startup
transaction = Transaction()
