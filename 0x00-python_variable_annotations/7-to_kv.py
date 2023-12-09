#!/usr/bin/env python3
'''Module for Task 7: Key-Value Conversion.
'''
from typing import Union, Tuple

def to_kv(key: str, value: Union[int, float]) -> Tuple[str, float]:
    '''Converts a key and its value to a tuple, with the key
    unchanged and the value squared.
    '''
    return (key, float(value**2))

