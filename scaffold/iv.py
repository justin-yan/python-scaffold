from __future__ import annotations
from collections import deque, defaultdict, namedtuple, OrderedDict, Counter
from itertools import chain, permutations
from typing import List, Any, Callable, Dict, Deque, NamedTuple, Optional, Counter
from queue import PriorityQueue

def test(num: int) -> int:
    return num + 2

if __name__ == '__main__':
    print(test(2))