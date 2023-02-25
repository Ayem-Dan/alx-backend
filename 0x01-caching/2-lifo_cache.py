#!/usr/bin/python3
"""Module for LIFOCache class that inherits from BaseCaching and is a \
      caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """Constructor method"""
        super().__init__()

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item value for \
        the key"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

        self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
