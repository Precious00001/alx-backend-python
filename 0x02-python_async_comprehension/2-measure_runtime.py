#!/usr/bin/env python3
'''
    Description: Measure the runtime of async_comprehension
    executed 4 times in parallel.
'''
from asyncio import gather
from time import time

# Import the async_comprehension coroutine from module '1-async_comprehension'
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    This function calculates the total time taken
    to execute the async_comprehension
    coroutine four times in parallel using asyncio.gather.

    Purpose:
    - Demonstrates the concurrent execution
    of async_comprehension.
    - Measures the performance of async_comprehension
    in a parallel setting.

    Returns:
    float: The total runtime of executing
    async_comprehension 4 times in parallel.
    '''
    first_time = time()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    next_time = time()

    return next_time - first_time
