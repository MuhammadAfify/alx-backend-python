#!/usr/bin/env python3
"""type-annotated function sum_list which takes a list input_list of floats"""

from type import list
def sum_list(input_list: list[float]) -> float:
    """returns their sum as a float"""
    a: float = 0.0
    for idx in input_list:
        a += idx
    return a

