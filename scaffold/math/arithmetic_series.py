from typing import List


# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/
# The overall approach is pretty straight-fowardly "greedy" - you always want to sell from the biggest remaining pile.
# When two piles are the same, you alternative drawing from them until they reach the size of the third largest pile... and so on.
# However, the test cases are set up like [100000000, 100000000, 100000000, 100000000], 100000000 - which will result
# in a huge number of iterations if you go one by one.
# The key insight is that you can use the identity (1 + 2 + 3 + ... + n) = n(n+1)/2 to calculate many iterations in a "single" shot:
# [100000000, 200000, 40000, 8000] -> [200000, 200000, 40000, 8000] -> [40000, 40000, 40000, 8000] -> [8000, 8000, 8000, 8000] -> [0, 0, 0, 0]
# Each arrow is should require just a single set of multiplications.
def maxProfit(inventory: List[int], orders: int) -> int:
    # Start by sorting the inventory.
    inventory.sort()
    # This variable keeps track of how many stacks are currently being drawn from
    current_max_stacks = 0
    remaining_orders = orders
    total = 0
    while remaining_orders > 0:
        try:
            current_max = inventory.pop()  # Take the largest element
        except IndexError as e:
            return total
        current_max_stacks += 1
        next_max = 0 if len(inventory) == 0 else inventory[-1]
        # We want to draw from each color in current_max_stacks equally until we either draw all remaining, or hit the next max stack.
        number_to_draw = min(remaining_orders, (current_max - next_max) * current_max_stacks)
        fromeachcolor, remaindertospread = divmod(number_to_draw, current_max_stacks)
        # for from each color, we use a simple arithmetic sequence to compute the total
        totalfromeachcolor = (current_max * fromeachcolor) - (fromeachcolor - 1) * (fromeachcolor) // 2
        total += totalfromeachcolor * current_max_stacks
        # for the remainder, we subtract fromeachcolor from the currentmax.  The first ball is at (current_max - 0), so the one *after* we've drawn fromeach color is at current_max - fromeachcolor cost
        remaindertotalpercolor = current_max - fromeachcolor
        total += remaindertotalpercolor * remaindertospread
        remaining_orders -= number_to_draw

    return total % (10 ** 9 + 7)
