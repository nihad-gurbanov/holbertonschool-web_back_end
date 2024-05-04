#!/usr/bin/env python3

"""
    It is a type-annotated function to_str that takes a float n as argument
    and returns the string representation of the float.
"""


def to_str(n: float) -> str:
    """
    Converts a float to its string representation.

    Parameters:
        n (float): The number to be converted to a string.

    Returns:
        str: The string representation of the input number.

    Examples:
        >>> to_str(3.14)
        '3.14'
        >>> to_str(-5.7)
        '-5.7'
    """
    return str(n)
