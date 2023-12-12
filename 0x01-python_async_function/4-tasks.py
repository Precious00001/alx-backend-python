#!/usr/bin/env python3
'''
Description: Take the code from wait_n and alter it
            into a new function task_wait_n.
            The code is nearly identical to wait_n
            except task_wait_random is being called.
'''

import asyncio
from typing import List
from time import time

# Import the task_wait_random function from the previous file
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Spawn task_wait_random n times with the specified max_delay.

    Parameters:
    - n (int): The number of times to spawn task_wait_random.
    - max_delay (int): The maximum
    delay for each task_wait_random call.

    Returns:
    List[float]: A list of delays (float values)
    in ascending order.
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
