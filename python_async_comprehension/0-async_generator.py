#!/usr/bin/env python3


"""
    It is  a coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module.
"""


import asyncio
import random


async def async_generator():
    """
    Asynchronous generator that yields a random number between 0 and 10 after
    asynchronously waiting for 1 second, repeated 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
