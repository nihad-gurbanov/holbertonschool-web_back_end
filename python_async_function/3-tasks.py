#!/usr/bin/env python3

"""
    It is a function task_wait_random that takes an integer max_delay
    and returns a asyncio.Task.
"""


import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that returns an asyncio.Task for wait_random coroutine.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: Task object for wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
