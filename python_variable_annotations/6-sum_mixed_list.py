#!/usr/bin/env python3

"""
    It is a type-annotated function sum_mixed_list which takes a list mxd_lst
    of integers and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Calculates the sum of all elements in a list containing either
        floats or integers.

        Parameters:
            mxd_lst (Union[List[float], List[int]]): A list containing
            either floats or integers.

        Returns:
            float: The sum of all elements in the mixed list.
    """
    return sum(mxd_lst)
