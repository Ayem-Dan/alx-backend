#!/usr/bin/python3
"""Module for FIFOCache class that inherits from BaseCaching and is a \
      caching system"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """Constructor method"""
        super().__init__()
        self.key_list = []

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item value for \
        the key"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.key_list.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}\n")
            self.key_list.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
