#!/usr/bin/env python3
"""Basic cache module"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache - Basic cache function that inherite from BaseCaching
    """
    def put(self, key, item):
        """Assign a key value to dictionary"""
        if key and item:
            self.cache_data[key] = item


    def get(self, key):
        """Returns the key value linked to parent cache"""
        if key is None or key not in self.cache_data.key():
            return None
        return self.cache_data[key]
