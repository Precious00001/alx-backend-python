#!/usr/bin/env python3
''' Description: Import async_generator from the previous task and then write
                 a coroutine called async_comprehension
                 that takes no arguments.
                 The coroutine uses async comprehension
                 over async_generator
                 to collect 10 random numbers,
                 then returns the list of 10 random
                 numbers.
'''

from typing import List

# Import the async_generator coroutine from module '0-async_generator'
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Return a list of values yielded by async_generator
    using async comprehension.

    Returns:
    List[float]: A list containing 10 random numbers.
    '''
    return [value async for value in async_generator()]
