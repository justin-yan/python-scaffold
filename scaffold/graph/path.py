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
    while not search_queue.empty():
        effort, x, y = search_queue.get()
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
                    search_queue.put((proposed_path_effort, candrow, candcol))
    return efforts[numrows - 1][numcols - 1]


# https://leetcode.com/problems/path-with-maximum-probability/
# Probability on edges combines multiplicatively and will monotonically decrease, which means expanding by the largest probability
# will make any total-path probability calculation inductively optimal, so djikstra's should work.
# Track probabilities for each node, initialize to 0.  Initialize start node to 1.  Loop until last node.
# Pop from priority queue.
# Take all legal neighbors, calculate new effort by taking current node and multiplying by edge probability.
# Update effort graph if probability is higher, and add to priority queue to search ordered by best full path probability.
# return 0 if there is no path (i.e. exit loop, but not at end)
def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    probabilities = [0.0 for i in range(n)]
    probabilities[start] = 1.0
    adjacencymatrix = defaultdict(set)
    for idx, edge in enumerate(edges):
        adjacencymatrix[edge[0]].add((edge[1], idx))
        adjacencymatrix[edge[1]].add((edge[0], idx))
    search_queue = PriorityQueue()
    search_queue.put((1, start))
    while not search_queue.empty():
        stepprob, node = search_queue.get()
        if node == end:
            return probabilities[node]
        for neighbor, edgeindex in adjacencymatrix[node]:
            curprob = probabilities[node]
            stepprob = curprob * succProb[edgeindex]
            if probabilities[neighbor] < stepprob:
                probabilities[neighbor] = stepprob
                # We want the largest values first, so we need to reverse the priority queue search order
                search_queue.put((-stepprob, neighbor))
    return 0


if __name__ == "__main__":
    # minimumEffortPath([[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]])
    print(maxProbability(3, [[0,1]], [.5], 0, 2))
