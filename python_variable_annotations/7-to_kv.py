#!/usr/bin/env python3
from typing import Union, Tuple

"""
    It is a type-annotated function to_kv that takes a string k and an int OR
    float v as arguments and returns a tuple. The first element of the tuple is
    the string k. The second element is the square of the int/float v and
    should be annotated as a float.
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Creates a tuple where the first element is the key `k` and the second
        element is the square of the value `v`.

        Parameters:
            k (str): The key.
            v (Union[int, float]): The value, which can be either an integer
            or a float.

        Returns:
            Tuple[str, float]: A tuple containing the key `k` and the square
            of the value `v`.
    """
    return k, v ** 2
