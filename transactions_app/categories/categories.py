from transactions_app.categories.category import Category
from transactions_app.utils.base_collector import BaseCollector
from transactions_app.utils.singleton import Singleton


class Categories(Singleton, BaseCollector):
    collection: dict = {}

    def get_or_create(self, category_name: str):
        if not category_name in self.collection:
           self.collection[category_name] = Category(category_name)
        return self.collection[category_name]

    def get_cashback(self, category_name: str, transaction_month: str):
        rotating_categories = {'January': 'travel',
                               'February': 'restaurant',
                               'March': 'retail',
                               'April': 'entertainment',
                               'May': 'bar',
                               'June': 'travel',
                               'July': 'restaurant',
                               'August': 'retail',
                               'September': 'entertainment',
                               'October': 'bar',
                               'November': 'restaurant',
                               'December': 'retail'}
        if rotating_categories[transaction_month] == category_name:
            return 5
        return 1
