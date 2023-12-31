#!/usr/bin/env python3
'''Task 2's module.
'''


def floor(n: float) -> int:
    ''' Return largest int value less than or equal to n. '''
    return int(n) if n >= 0 else int(n) - 1
