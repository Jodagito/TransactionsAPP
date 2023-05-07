from datetime import datetime

from transactions_app.categories import Categories
from transactions_app.utils.base_holder import BaseTransactionsHolder


class Account(BaseTransactionsHolder):
    def __init__(self, account_id: int, cash_back_bound: float = 100):
        self.id: int = account_id
        self.cash_back: float = 0
        self.cash_back_rotative: float = 0
        self.cash_back_bound: float = cash_back_bound
        super().__init__()

    def add_transaction(self, transaction):
        super().add_transaction(transaction)
        self._calculate_cashback(transaction)

    def _calculate_cashback(self, transaction):
        """
        Gets the cash back percentage for the month and category,
        then calculates the cashback by multiplying the transaction amount and the percentage.

        Checks if the cash back percentage is equal to 5%, then checks if the
        cash back rotative is lower than the cash back limit for rotative categories,
        and finally checks if the current transaction cash back is
        lower than the remaining cash back before limit.
        If everything is True then adds the transaction cash back to the count.

        If current transaction cash back is bigger than the remaining cash back before limit,
        then we calculate the remaining cash back before limit, and divide the transaction amount in two.
        First portion amount is calculated by dividing the remaining cash back by the cash back percentage,
        which is 5% in this case.

        Second portion is calculated by substracting the first portion from the transaction amount.
        Then calculates the 5% of the first portion and add it to the rotative cash back count,
        the second portion is added to the cash back.

        Finally if the cash back percentage is 1% then the transaction cash back is added to the count.
        """
        transaction_month = datetime.strftime(transaction.transaction_date, "%B")
        cash_back_percentage = Categories().get_cashback(transaction.category.name, transaction_month)/100
        cash_back = transaction.amount * cash_back_percentage
        if (cash_back_percentage == 0.05 and
            self.cash_back_rotative < self.cash_back_bound and
            cash_back <= self.cash_back_bound - self.cash_back_rotative):
            self.cash_back_rotative += cash_back
        elif cash_back_percentage == 0.05 and self.cash_back_rotative < self.cash_back_bound:
            remaining_cash_back = self.cash_back_bound - self.cash_back_rotative
            first_portion = remaining_cash_back / cash_back_percentage
            second_portion = transaction.amount - first_portion
            self.cash_back_rotative += first_portion * cash_back_percentage
            self.cash_back += second_portion * 0.01
        else:
            self.cash_back += cash_back

    def get_cash_back(self):
        return self.cash_back + self.cash_back_rotative
