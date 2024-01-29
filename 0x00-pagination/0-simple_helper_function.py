#!/usr/bin/env python3
"""Function index module"""

from typing import Tuple


def index_range(page: int,  page_size: int) -> Tuple[int, int]:
    """
    index_range - Function that specify an index
    @page: The page number
    @page_size: The size  of each page
    Return: Tuple list of indices
    """
    start_idx = (page - 1) * page_size
    return (start_idx, start_idx + page_size)
