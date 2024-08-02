#!/usr/bin/env python3
"""type-annotated function takes a float"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float"""
    return lambda x: x * multiplier
