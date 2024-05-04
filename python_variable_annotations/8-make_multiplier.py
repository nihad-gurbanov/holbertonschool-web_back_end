#!/usr/bin/env python3

"""
    It is a type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies a float
    by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Returns a function that multiplies a float by the given multiplier.

        Parameters:
            multiplier (float): The multiplier to be used.

        Returns:
            Callable[[float], float]: A function that takes a float and returns
            the product of that float and the multiplier.
        """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
