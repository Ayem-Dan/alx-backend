"""Module of BasicCache class inheriting BaseCaching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Methods used in the class"""
    def put(self, key, item):
        """defines the key and items"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the key and items"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
