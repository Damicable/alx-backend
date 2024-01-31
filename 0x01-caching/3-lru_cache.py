#!/usr/bin/env python3
"""LRUCache module"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache - Class LRU cache that inherits from BaseCaching
    """
    def __init__(self):
        """Override init"""
        super().__init__()
