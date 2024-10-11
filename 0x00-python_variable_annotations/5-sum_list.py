#!/usr/bin/env python3
''' Complex typesmodule.
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Computing the sum of a list of floating-point numbers.
    '''
    return float(sum(input_list))
