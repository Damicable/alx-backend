#!/usr/bin/env python3
"""FIFOCache module"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache - FIFO class that inherites from BaseCaching
    """
    def put(self, key, item):
        """This assigns item value for key to dic self.cache_data"""
        if key and item:
            self.cache_data[key] = item
        cache_keys = list(self.cache_data.keys())
        if len(cache_keys) > self.MAX_ITEMS:
            key_to_discard = cache_keys[0]
            self.cache_data.pop(key_to_discard)
            print("DISCARD: {}".format(key_to_discard))


    def get(self, key):
        """Returns the key value in self.cache_data"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
