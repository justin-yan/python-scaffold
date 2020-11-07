from collections import defaultdict
import random
from typing import List, Optional


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        # You could instantiate an index of all list values here, and pick would become an O(1) operation

    def pick(self, target: int) -> Optional[int]:
        # index = []
        # for idx, val in enumerate(self.nums):
        #     if val == target:
        #         index.append(idx)
        # count = len(index)
        # return index[random.randint(0, count - 1)]

        # One way to avoid building up extraneous state is to use the identity
        # 1/2 * 2/3 * ... * (n-1)/n = 1/n
        # You don't know n at first, but if you give earlier elements a higher probability and force them to go through progressively weaker checks, you can converge to 1/n

        result = None
        count = 0
        for idx, val in enumerate(self.nums):
            if val == target:
                if random.randint(0, count) == count:
                    result = idx
                count += 1
        return result
