import stat
from fastapi import FastAPI, Response, status

# creating app as instance of FastAPI
app = FastAPI()


# setting our default get request for the "/" url as a welcome message to test uvicorn
@app.get("/")
def root():
    return {"message": "Welcome to my api!!!"}


# PUT request to add coin
@app.put("/")
def add_coin(response: Response):
    response.status_code = status.HTTP_204_NO_CONTENT
    pass


# DELETE request to return coins
@app.delete("/")
def return_coins(response: Response):
    response.status_code = status.HTTP_204_NO_CONTENT
    pass


# GET request for global inventory in vending machine
@app.get("/inventory")
def get_machine_inventory():
    pass


# GET request for individual item inventory
@app.get("/inventory/{id}")
def get_item_inventory(id: int):
    pass


# PUT request for vending item
@app.put("/inventory/{id}")
def vend_item(id: int):
    pass


# PUT request for resource/item not found or out of stock 404
@app.put("/inventory/{id}")
def resource_not_found(id: int, response: Response):
    response.status_code = status.HTTP_404_NOT_FOUND
    pass


# PUT request for currency below purchase price 403
@app.put("/inventory/")
def currency_below_purchase_price(response: Response):
    response.status_code = status.HTTP_403_FORBIDDEN
    pass
