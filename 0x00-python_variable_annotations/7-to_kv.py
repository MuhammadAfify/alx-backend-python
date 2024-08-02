#!/usr/bin/env python3
"""type-annotated function that takes a string and an int OR float
    as arguments"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple od srtings and float"""
    sqr = v **2
    return (k, sqr)
