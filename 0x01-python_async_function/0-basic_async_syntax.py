#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay"""
    randNum = random.uniform(0, max_delay)
    await asyncio.sleep(randNum)
    return randNum
