class Transaction:
    def __init__(self):
        self.coin_count = 0

    def get_coin_count(self):
        return self.coin_count

    def set_coin_count(self, value: int):
        self.coin_count = value

    def test_coin_count(self):
        if self.coin_count >= 2:
            return True
        else:
            return False

    def clear_coin_count(self):
        self.coin_count = 0
