from collections import deque, defaultdict, namedtuple, OrderedDict, Counter
from itertools import chain, permutations
from typing import List, Any, Callable, Dict, Deque, NamedTuple, Optional, Counter
from queue import PriorityQueue

# https://leetcode.com/problems/path-with-minimum-effort/
# Height exhibits a monotonicity property, in that expanding the search by the shortest connected height cannot
# result in an incorrect min-height calculation, since expanding by any larger height will automatically make the total-path cost
# more than the alternative.  This means a djikstra's style search should work just fine.
# Track efforts for each node.  In theory, a node's effort can only go up the way we're searching, so
# we want to initialize the efforts to infinity, and if we can get to a node cheaper than it currently allows,
# we'll want to update it, and then add it to the search queue so we can investigate its neighbors.
# Starting at the top left, and until we reach the bottom right:
# pop from priority queue
# Take all legal neighbors, update their efforts and add them to the priority queue, if unvisited
def minimumEffortPath(heights: List[List[int]]) -> int:
    numrows, numcols = len(heights), len(heights[0])
    efforts = [[9999999 for i in range(numcols)] for j in range(numrows)]
    efforts[0][0] = 0
    search_queue = PriorityQueue()
    search_queue.put((0, 0, 0))
    while search_queue:
        marg_effort, x, y = search_queue.get()
        if (x, y) == (numrows - 1, numcols - 1):
            return efforts[x][y]
        for rowdelta, coldelta in [(1,0),(0,1),(-1,0),(0,-1)]:
            candrow, candcol = x + rowdelta, y + coldelta
            if 0 <= candrow < numrows and 0 <= candcol < numcols:
                currentpatheffort = efforts[x][y]
                marginaleffort = abs(heights[candrow][candcol] - heights[x][y])
                proposed_path_effort = max(currentpatheffort, marginaleffort)
                # We only update the effort matrix if we are improving the path.
                # Additionally, because we're using a monotonic and min-greedy search,
                # we will only visit every node once, which means that this condition
                # will also prevent us from adding any node to the search queue twice.
                if efforts[candrow][candcol] > proposed_path_effort:
                    efforts[candrow][candcol] = proposed_path_effort
                    search_queue.put((marginaleffort, candrow, candcol))
    return efforts[numrows - 1][numcols - 1]

if __name__ == "__main__":
    minimumEffortPath([[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]])