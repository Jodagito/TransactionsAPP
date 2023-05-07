from abc import ABC, abstractclassmethod


class BaseCollector(ABC):
    collection: dict

    @abstractclassmethod
    def get_or_create(self, object_id):
        pass
