#!/usr/bin/env python3

"""
    It is a type-annotated function floor which takes a float n as argument and
    returns the floor of the float.
"""


def floor(n: float) -> int:
    """
    Returns the largest integer less than or equal to a given number.

    Parameters:
        n (float): The number for which the floor value is to be calculated.

    Returns:
        int: The floor value of the given number.

    Examples:
        >>> floor(4.9)
        4
        >>> floor(-3.2)
        -4
    """
    return int(n // 1)
