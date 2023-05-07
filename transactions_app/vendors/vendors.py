from transactions_app.vendors.vendor import Vendor
from transactions_app.utils.base_collector import BaseCollector
from transactions_app.utils.singleton import Singleton


class Vendors(Singleton, BaseCollector):
    collection: dict = {}

    def get_or_create(self, vendor_id: int, vendor_name: str = None):
        if not vendor_id in self.collection:
           self.collection[vendor_id] = Vendor(vendor_id, vendor_name)
        return self.collection[vendor_id]
