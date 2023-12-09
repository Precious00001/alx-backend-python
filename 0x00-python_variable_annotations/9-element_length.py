#!/usr/bin/env python3
'''Module for Task 7: Key-Value Tuple Conversion.
'''
from typing import Union, Tuple

def to_kv(key: str, value: Union[int, float]) -> Tuple[str, float]:
    '''Converts a given key and its associated value into a tuple
    where the key remains unchanged, and the value is squared.
    '''
    return (key, float(value ** 2))
