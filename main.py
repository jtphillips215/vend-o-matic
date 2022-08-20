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


# instatiating 3 items to add to machine
inventory = []
for i in range(3):
    item = Item(i)
    inventory.append(item)

# creating transaction for machine on startup
transaction = Transaction()


# setting our default get request for the "/" url as a welcome message to test uvicorn
@app.get("/")
def root():
    return {"message": "Welcome to my api!!!"}


# PUT request to add coin
@app.put("/", status_code=status.HTTP_204_NO_CONTENT)
def add_coin(inserted_coin: Coin):
    increment_coins(inserted_coin)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# DELETE request to return coins
@app.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def return_coins(response: Response):
    response.headers["X-Coins"] = f"{transaction.coin_count}"


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


# PUT request for vending item
@app.put("/inventory/{id}")
def vend_item(id: int):
    pass


# PUT request for resource/item not found or out of stock 404
@app.put("/inventory/{id}", status_code=status.HTTP_404_NOT_FOUND)
def resource_not_found(id: int):
    pass


# PUT request for currency below purchase price 403
@app.put("/inventory/{id}", status_code=status.HTTP_403_FORBIDDEN)
def currency_below_purchase_price():
    pass
