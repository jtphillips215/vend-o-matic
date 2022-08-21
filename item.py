class Item:
    def __init__(self, id):
        self.id = id
        self.quantity = 5

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity: int):
        self.quantity = quantity

    def get_id(self):
        return self.id

    def test_quantity(self):
        if self.quantity >= 1:
            return True
        else:
            return False
