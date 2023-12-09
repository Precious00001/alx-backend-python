#!/usr/bin/env python3
'''Module for Task 8: Creating a multiplier function.
'''
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Generates a function that multiplies a given number by a specified multiplier.

    Args:
    multiplier (float): The value to multiply by.

    Returns:
    Callable[[float], float]: A lambda function that takes a float argument and returns the result of the multiplication.
    '''
    return lambda x: x * multiplier

