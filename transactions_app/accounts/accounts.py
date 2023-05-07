from transactions_app.accounts.account import Account
from transactions_app.utils.base_collector import BaseCollector
from transactions_app.utils.singleton import Singleton


class Accounts(Singleton, BaseCollector):
    collection: dict = {}

    def get_or_create(self, account_id: int):
        if not account_id in self.collection:
           self.collection[account_id] = Account(account_id)
        return self.collection[account_id]
