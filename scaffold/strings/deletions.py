from collections import Counter


# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
# The idea is pretty straightforward:
# Generate a frequency distribution of characters.
# The problem has the property that in the event of a conflict, it doesn't actually matter *which* character gets deleted.
# I.e. aaaabbbbccc -> bbbbcccaa vs. bbbbaaacc requires the same number of deletions.
# Therefore, you just want to fill in frequency slots as "cheaply" as possible.
# So we loop over the frequency hashmap, and make the minimal number of deletions to slot into frequency slots (tracked by set)
def minDeletions(self, s: str) -> int:
    frequencies = Counter(s)
    frequencyslots = set()
    deletions = 0
    for char in frequencies.keys():
        while frequencies[char] > 0:
            if frequencies[char] in frequencyslots:
                frequencies[char] -= 1
                deletions += 1
            else:
                frequencyslots.add(frequencies[char])
                break
    return deletions
