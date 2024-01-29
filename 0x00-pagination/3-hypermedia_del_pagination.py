#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        get_hyper_index - Indexing that's resistant to deletions
        @index: Int, The current start index to start with
        @page_size: Int, size of dataset to return
        """
        database_index = self.indexed_dataset()
        assert isinstance(index, int) and index < len(database_index) - 1
        data_section = []
        page_tracker = 0
        data_tracker = index
        next_index = None
        while page_tracker < page_size:
            val = database_index.get(page_tracker + index, None)
            page_tracker += 1
            if val:
                data_section.append(val)
                data_tracker += 1

        while data_tracker < len(database_index):
            val = database_index.get(data_tracker, None)
            if val:
                next_index = data_tracker
                break
            data_tracker += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data_section
        }
