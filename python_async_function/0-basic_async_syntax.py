#!/usr/bin/env python3

"""
    It is an asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random that waits for
    a random delay between 0 and max_delay (included and float value) seconds
    and eventually returns it.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between
    0 and max_delay seconds (inclusive).

    Args:
        max_delay (int, optional): Maximum delay in seconds (default is 10).

    Returns:
        float: The random delay that was waited for.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
