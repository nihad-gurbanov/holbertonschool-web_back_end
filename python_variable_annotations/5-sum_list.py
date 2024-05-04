#!/usr/bin/env python3


"""
    It is a type-annotated function sum_list which takes a list input_list of
    floats as argument and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of all elements in the input list.

    Parameters:
        input_list (list[float]): A list of floating-point numbers.

    Returns:
        float: The sum of all elements in the input list.
    """
    return sum(input_list)
