#!/usr/bin/env python3

"""
    Annotate the below function’s parameters and return values with the
    appropriate types
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Returns a list of tuples containing each element of `lst` and
        its length.

        Parameters:
            lst (Iterable[Sequence]): An iterable containing sequences.

        Returns:
            List[Tuple[Sequence, int]]: A list of tuples, where each tuple
            contains a sequence from `lst` and its length.
    """
    return [(i, len(i)) for i in lst]
