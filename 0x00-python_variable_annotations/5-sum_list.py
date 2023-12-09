#!/usr/bin/env python3
''' 
Description: Calculates the sum of elements in a list of floats.
Arguments: 
    input_list (List[float]): A list of floats.
'''

from typing import List

def sum_list(input_list: List[float]) -> float:
    '''Returns the sum of all elements in the input_list.'''
    return sum(input_list)
