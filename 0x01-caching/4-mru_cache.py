#!/usr/bin/env python3
"""MRU cache 1 module"""


from datetime import datetime
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache - MRU cache class inheriting from BaseCaching
    """
    def __init__(self):
        """Override init"""
        super().__init__()
        self.access_log = {}

    def put(self, key, item):
        """Put value that sets key and item on parent dict"""
        if key and item:
            self.cache_data[key] = item
            key_to_discard = max(
                self.access_log, key=self.access_log.get) if len(
                    self.access_log) > 0 else None
            self.access_log[key] = datetime.now()
            if len(self.cache_data) > self.MAX_ITEMS:
                self.cache_data.pop(key_to_discard)
                self.access_log.pop(key_to_discard)
                print("DISCARD: {}".format(key_to_discard))

    def get(self, key):
        """Fetch the value of a given key in parent cache data"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.access_log[key] = datetime.now()
        return self.cache_data[key]
