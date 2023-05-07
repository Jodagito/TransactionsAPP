from transactions_app.utils.base_holder import BaseTransactionsHolder


class Category(BaseTransactionsHolder):
    def __init__(self, category_name: str):
        self.name = category_name
        super().__init__()
