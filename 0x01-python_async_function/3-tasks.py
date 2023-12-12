#!/usr/bin/env python3
'''
Description: Import wait_random from 0-basic_async_syntax.
             Write a function (do not create an async function,
             use the regular function syntax to do this) task_wait_random
             that takes an integer max_delay and returns an asyncio.Task.
'''

import asyncio

# Import the wait_random coroutine from the previous file
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Return an asyncio.Task for the wait_random
    coroutine with the given max_delay.

    Parameters:
    - max_delay (int): The maximum delay for the
    wait_random coroutine.

    Returns:
    asyncio.Task: An asyncio.Task object.
    '''
    return asyncio.create_task(wait_random(max_delay))
