class Item:
    def __init__(self, id):
        self._id = id
        self._quantity = 5

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity: int):
        self._quantity = quantity

    def get_id(self):
        return self._id

    def test_quantity(self):
        if self._quantity >= 1:
            return True
        else:
            return False
