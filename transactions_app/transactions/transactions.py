from transactions_app.transactions.transaction import Transaction
from transactions_app.utils.base_holder import BaseTransactionsHolder


class Transactions(BaseTransactionsHolder):
    def __init__(self, json_list: list[dict] = None):
        super().__init__()
        if json_list:
            self._create_transactions_from_json_list(json_list)

    def _create_transactions_from_json_list(self, json_list):
        mapped_keys = {'accountId': 'account_id', 'amount': 'amount', 'category': 'category',
                       'transactionId': 'transaction_id', 'transactionDate': 'transaction_date',
                       'vendorId': 'vendor_id', 'vendorName': 'vendor_name'}
        formatted_json_list = []
        for json_object in json_list:
            formatted_json_list.append({mapped_keys[key]: json_object[key] for key in json_object})
        self.transactions = [Transaction(**json_object) for json_object in formatted_json_list]
