#!/usr/bin/env python3

"""
    It is a measure_time function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay), and
    returns total_time / n. Your function should return a float.
"""


import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the execution time of the wait_n coroutine.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Execution time in seconds.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    exc_time = time.perf_counter() - start
    return exc_time
