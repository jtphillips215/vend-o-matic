class Transaction:
    def __init__(self):
        self.coin_count = 0

    # testing the coin count prior to vending items
    def test_coin_count(self):
        if self.coin_count >= 2:
            return True
        else:
            return False
