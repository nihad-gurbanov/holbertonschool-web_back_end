#!/usr/bin/env python3

"""
    Take the code from wait_n and alter it into a new function task_wait_n.
    The code is nearly identical to wait_n except task_wait_random
    is being called.
"""


import asyncio
from typing import List


wait_random = __import__("").wait_random

def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Regular function that creates asyncio.Tasks for wait_random coroutine.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        list: List of delays (float values) in ascending order.
    """
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(wait_random(max_delay)) for _ in range(n)]
    results = loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
    return sorted(results)
