from datetime import datetime
from uuid import UUID

from transactions_app.accounts import Account, Accounts
from transactions_app.categories import Category, Categories
from transactions_app.vendors import Vendor, Vendors


class Transaction:
    def __init__(self, account_id,
                 amount, category, transaction_id, transaction_date,
                 vendor_id, vendor_name, account_cash_back_bound = None):
        self.id = UUID(transaction_id)
        self.amount = amount
        self.transaction_date = datetime.fromisoformat(transaction_date)

        self.category: Category = Categories().get_or_create(category)

        self.account_id = account_id
        if account_cash_back_bound:
            self.account: Account = Accounts().get_or_create(account_id, account_cash_back_bound)
        else:
            self.account: Account = Accounts().get_or_create(account_id)
        self.account.add_transaction(self)

        self.vendor_id = vendor_id
        self.vendor_name = vendor_name
        self.vendor: Vendor = Vendors().get_or_create(vendor_id, vendor_name)
        self.vendor.add_transaction(self)
