#!/usr/bin/python3
"""Module for LRUCache class that inherits from BaseCaching and is a \
      caching system"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class that inherits from BaseCaching"""

    def __init__(self):
        """Constructor method"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item value \
              for the key key"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.keys.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD: {}".format(lru_key))

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None

        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
