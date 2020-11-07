# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from typing import Dict


def lengthOfLongestSubstring(self, s: str) -> int:
    # A greedy-ish solution works, but the idea is that when you hit the second instance of a char
    # you update the starting point from which you are considering substrings
    # you move the cursor *forward* to the char after the previous instance you had seen
    start = maxLength = 0
    charViewedHash: Dict[str, int] = {}
    for idx in range(len(s)):
        char = s[idx]
        if char in charViewedHash and start <= charViewedHash[char]:
            # This is a dupe and keeps cursor moving monotonically forward
            start = charViewedHash[char] + 1
            # maxLength does not change since we are removing one from the start, and adding one to the tail.
        else:
            maxLength = max(maxLength, idx - start + 1)
        charViewedHash[char] = idx
    return maxLength