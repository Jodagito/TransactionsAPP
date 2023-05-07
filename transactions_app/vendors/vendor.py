from transactions_app.utils.base_holder import BaseTransactionsHolder


class Vendor(BaseTransactionsHolder):
    def __init__(self, vendor_id: int, vendor_name: str):
        self.id = vendor_id
        self.name = vendor_name
        super().__init__()
