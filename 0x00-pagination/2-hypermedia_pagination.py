#!/usr/bin/env python3
"""Function index module"""


import csv
import math
from typing import List, Tuple


def index_range(page: int,  page_size: int) -> Tuple[int, int]:
    """
    index_range - Function that specify an index
    @page: The page number
    @page_size: The size  of each page
    Return: Tuple list of indices
    """
    start_idx = (page - 1) * page_size
    return (start_idx, start_idx + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get_page - function to get the specified pages from csv file
        @page: Page number to fetch
        @page_size: Size of page to fetch
        Returns: List of pages to fetch
        """
        for in_val in [page, page_size]:
            assert isinstance(in_val, int)
            assert in_val > 0
        (start_idx, end_idx) = index_range(page, page_size)
        dataset_val = self.dataset()
        if end_idx > len(dataset_val):
            return []
        return dataset_val[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        get_hyper - Gets the specified pages from csv file and returns a dict
        @page: Page to fetch
        @page_size: Size of page to fetch
        Returns: A dictionary
        """
        for in_val in [page, page_size]:
            assert isinstance(in_val, int)
            assert in_val > 0
        (start_idx, end_idx) = index_range(page, page_size)
        dataset_val = self.dataset()
        data_len = len(dataset_val)
        data = []
        if end_idx <= data_len:
            data = dataset_val[start_idx:end_idx]
        next_page = None
        if data_len >= end_idx:
            next_page = page + 1
        prev_page = None
        if page > 1:
            prev_page = page - 1
        total_pages = data_len // page_size
        if data_len % page_size != 0:
            total_pages = (data_len // page_size) + 1
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
