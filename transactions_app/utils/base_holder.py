class BaseTransactionsHolder:
    def __init__(self):
        self.transactions: list = []

    def add_transaction(self, transaction):
        if transaction not in self.transactions:
            self.transactions.append(transaction)
