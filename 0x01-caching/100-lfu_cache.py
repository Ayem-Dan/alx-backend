#!/usr/bin/python3
"""LFU Caching"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Class LFUCache inherits from BaseCaching"""

    def __init__(self):
        """ Initiliaze LFUCache """
        super().__init__()
        self.freq = {}
        self.lfu = 0

    def update_frequency(self, key):
        """Update the frequency of the key"""
        frequency = self.freq.get(key, 0) + 1
        self.freq[key] = frequency

        if frequency > self.lfu:
            self.lfu = frequency

    def get_least_frequent_keys(self):
        """Get the keys with the least frequency"""
        keys = [key for key in self.cache_data if self.freq[key] == 1]
        if not keys:
            return None
        return keys

    def get_least_recently_used_key(self, keys):
        """Get the least recently used key"""
        lru_key = None
        lru_time = float('inf')
        for key in keys:
            if self.cache_data[key][1] < lru_time:
                lru_time = self.cache_data[key][1]
                lru_key = key
        return lru_key

    def remove_least_frequent(self):
        """Remove the least frequent item"""
        keys = self.get_least_frequent_keys()
        if keys is None:
            return
        lru_key = self.get_least_recently_used_key(keys)
        del self.cache_data[lru_key]
        del self.freq[lru_key]
        print("DISCARD: {}".format(lru_key))

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item value
           for the key key"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = (item, self.cache_data[key][1])
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.remove_least_frequent()
            self.cache_data[key] = item

        self.update_frequency(key)

    def get(self, key):
        """Return the value linked to key in self.cache_data"""
        if key is None or key not in self.cache_data:
            return None

        value, time = self.cache_data[key]
        self.cache_data[key] = (value, time + 1)
        self.update_frequency(key)

        return value
