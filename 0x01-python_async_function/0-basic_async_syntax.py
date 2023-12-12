#!/usr/bin/env python
''' Task: A coroutine called async_generator that takes no
                 arguments.
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random
    delay between 0 and max_delay seconds.

    Parameters:
    - max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
    - float: The random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
