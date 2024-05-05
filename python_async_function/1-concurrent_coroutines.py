#!/usr/bin/env python3

"""
    an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay. You will spawn wait_random n times
    with the specified max_delay.
"""


import asyncio
from typing import List

wait_random_module = __import__('0-basic_async_syntax')
wait_random = wait_random_module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with
    the specified max_delay.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        list: List of delays (float values) in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
