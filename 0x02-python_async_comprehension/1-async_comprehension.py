#!/usr/bin/env python3
"""collect 10 random numbers using an async comprehensing"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects async generated list and return it"""
    return [_ async for _ in async_generator()]
