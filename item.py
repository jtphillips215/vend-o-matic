class Item:
    def __init__(self, id):
        self.id = id
        self.quantity = 5

    # testing the item quatity prior to vending items
    def test_quantity(self):
        if self.quantity >= 1:
            return True
        else:
            return False
