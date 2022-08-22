class Transaction:
    def __init__(self):
        self._coin_count = 0

    def get_coin_count(self):
        return self._coin_count

    def set_coin_count(self, value: int):
        self._coin_count = value

    def test_coin_count(self):
        if self._coin_count >= 2:
            return True
        else:
            return False

    def clear_coin_count(self):
        self._coin_count = 0
