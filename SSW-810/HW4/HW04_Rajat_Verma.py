# -*- coding: utf-8 -*-
"""
Created on Sat Oct 4 2020
by - Rajat Verma
"""


import random
import unittest
from typing import Any, List, Optional, Sequence, Iterator

# PART 1

def count_vowels(s: str) -> int:
    ''' return the number of vowels in the string s '''
    count: int = 0
    s1: str = s.lower()
    for i in s1:
        if i in ['a', 'e', 'i', 'o', 'u']:
            count+=1
    return count

# PART 2

def find_last(target: Any, seq: Sequence[Any]) -> Optional[int]:
    ''' return the offset from 0 of the last occurrence of target in seq '''
    index : Optional[int] = None
    for idx, i in enumerate(seq):
        if i == target:
            index = int(idx)
    return index
  
# PART 3 is Fraction.simplify()

# PART 4
def my_enumerate(seq: Sequence[Any]) -> Iterator[Any]:
    """ emulate the behavior of Python's built in enumerate() function.
        For each call, return a tuple with the offset from 0 and the next item
    """
    for current in range(len(seq)):
        yield current, seq[current]