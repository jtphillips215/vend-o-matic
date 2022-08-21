from urllib import response
from fastapi import FastAPI, Response, status, HTTPException, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# creating app as instance of FastAPI
app = FastAPI()


# creating class for items to add to machine
class Item:
    def __init__(self, id):
        self.id = id
        self.quantity = 5


# class for transaction
class Transaction:
    def __init__(self):
        self.coin_count = 0


# pydantic schema for coin for / PUT request
class Coin(BaseModel):
    coin: int


# function for accessing item quantities as array
def get_quantities():
    quantities = []
    for item in inventory:
        quantities.append(item.quantity)
    return quantities


# function for getting the item quantity for a single item
def get_item_quantity(id: int):
    for item in inventory:
        if item.id == id:
            return item


# function for incrementing coin count
def increment_coins(inserted_coin: Coin):
    transaction.coin_count += inserted_coin.coin


# testing the coin count prior to vending items
def test_coin_count():
    if transaction.coin_count >= 2:
        return True
    else:
        return False


# testing the item quatity prior to vending items
def test_quantity(item):
    if item.quantity >= 1:
        return True
    else:
        return False


# instatiating 3 items to add to machine
inventory = []
for i in range(3):
    item = Item(i)
    inventory.append(item)

# creating transaction with coin count of 0 for machine on startup
transaction = Transaction()


# PUT request to add coin
@app.put("/", status_code=status.HTTP_204_NO_CONTENT)
def add_coin(inserted_coin: Coin, response: Response):
    increment_coins(inserted_coin)
    response.headers["X-Coins"] = f"{transaction.coin_count}"


# DELETE request to return coins
@app.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def return_coins(response: Response):
    response.headers["X-Coins"] = f"{transaction.coin_count}"
    transaction.coin_count = 0


# GET request for global inventory in vending machine
@app.get("/inventory")
def get_machine_inventory():
    quantities = get_quantities()
    return quantities


# GET request for individual item inventory
@app.get("/inventory/{id}")
def get_item_inventory(id: int):
    item = get_item_quantity(id)
    return item.quantity


# PUT request for vending item, returns status code and updates header if can't vend items
@app.put("/inventory/{id}")
def vend_item(id: int, response: Response):
    # checking coin count prior to inventory as coin count won't require querying data source for inventory
    # if held seperately like in a database
    # could reverse order if differently priced items were added to machine at later date
    if test_coin_count():
        if test_quantity(inventory[id]):
            pass
        else:
            response.headers["X-Coins"] = f"{transaction.coin_count}"
            response.status_code = status.HTTP_404_NOT_FOUND
    else:
        response.headers["X-Coins"] = f"{transaction.coin_count}"
        response.status_code = status.HTTP_403_FORBIDDEN


# PUT request for resource/item not found or out of stock 404
# @app.put("/inventory/{id}", status_code=status.HTTP_404_NOT_FOUND)
# def resource_not_found(id: int):
#    pass


# PUT request for currency below purchase price 403
# @app.put("/inventory/{id}", status_code=status.HTTP_403_FORBIDDEN)
# def currency_below_purchase_price():
#    pass
