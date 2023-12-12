#!/usr/bin/env python3
'''
Task 1's module: Async Comprehension.
'''
from typing import List
from importlib import import_module as using


# Import the async_generator coroutine from module '0-async_generator'
async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Creates a list of 10 numbers asynchronously
    using async comprehension.

    This coroutine leverages the async_generator,
    importing it from '0-async_generator'.
    It generates a list of 10 numbers by asynchronously
    iterating through the async_generator.

    Returns:
    List[float]: A list containing 10 numbers
    generated asynchronously.
    '''
    return [num async for num in async_generator()]
