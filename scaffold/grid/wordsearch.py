from collections import deque
from typing import List, Tuple, Set, Deque, Any


# https://leetcode.com/problems/word-search/
# Walk the grid looking for the initial letter in the word.
# From that point on, do a DFS.
def wordsearch_explicit_stack(board: List[List[str]], word: str) -> bool:
    wordlen = len(word)
    numrows = len(board)
    numcols = len(board[0])
    for rowidx in range(numrows):
        for colidx in range(numcols):
            if board[rowidx][colidx] == word[0]:
                # print("START DFS:", rowidx, colidx)
                # To do an iterative DFS, use an explicit stack.
                # Because we have to keep track of which nodes have been visited, we need to add both the depth
                # as well as the set of visited nodes along with the node to the stack in order to backtrack properly.
                nodestack: Deque[List[Any]] = deque()
                nodestack.append([rowidx, colidx, 0, {(rowidx, colidx)}])
                while nodestack:
                    node = nodestack.pop()
                    depth = node[2]
                    visited = node[3]
                    # print("DFS STEP:", node[0], node[1], depth)
                    if depth == wordlen - 1:
                        return True
                    for rowd, cold in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        candidaterow = node[0] + rowd
                        candidatecol = node[1] + cold
                        # print("NEIGHBOR:", candidaterow, candidatecol)
                        if 0 <= candidaterow < numrows and 0 <= candidatecol < numcols and (candidaterow, candidatecol) not in visited and board[candidaterow][candidatecol] == word[depth + 1]:  # Legal match
                            # print("HIT")
                            newvisited = visited.copy()
                            newvisited.add((candidaterow, candidatecol))
                            nodestack.append([candidaterow, candidatecol, depth + 1, newvisited])
    return False


def wordsearch_recursive(board: List[List[str]], word: str) -> bool:
    numrows = len(board)
    numcols = len(board[0])
    for rowidx in range(numrows):
        for colidx in range(numcols):
            if board[rowidx][colidx] == word[0]:
                # print("START DFS:", rowidx, colidx)
                if wordsearch_dfs_helper(board, word, rowidx, colidx, 0, {(rowidx, colidx)}):
                    return True
    return False


def wordsearch_dfs_helper(board: List[List[str]], word: str, rowidx: int, colidx: int, depth: int, visited: Set[Tuple[int, int]]) -> bool:
    if depth == len(word) - 1:
        return True
    # We are at rowidx, colidx, depth in the word, and our current position is in the visited set.
    for rowd, cold in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        candidaterow = rowidx + rowd
        candidatecol = colidx + cold
        if 0 <= candidaterow < len(board) and 0 <= candidatecol < len(board[0]) and (candidaterow, candidatecol) not in visited and board[candidaterow][candidatecol] == word[depth + 1]:
            # It's possible to save memory in the recursive version, because we have an opportunity to insert code in this stackframe
            # *after* the recursive calls have been completed, which means we could do bookkeeping on global board visibility
            # Whereas in the iterative version, we complete a stack frame before moving on to the next one, so if we hit a leaf,
            # we don't have a hook in which to clean up the entire path of visited letters.
            newvisited = visited.copy()
            newvisited.add((candidaterow, candidatecol))
            recresult = wordsearch_dfs_helper(board, word, candidaterow, candidatecol, depth + 1, newvisited)
            if recresult:
                return True
    return False

def wordsearch_dfs_helper_lowmem(board: List[List[str]], word: str, rowidx: int, colidx: int, depth: int) -> bool:
    if depth == len(word) - 1:
        return True
    board[rowidx][colidx] = "*"
    # We are at rowidx, colidx, depth in the word, and our current position is in the visited set.
    result = False
    for rowd, cold in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        candidaterow = rowidx + rowd
        candidatecol = colidx + cold
        if 0 <= candidaterow < len(board) and 0 <= candidatecol < len(board[0]) and board[candidaterow][candidatecol] == word[depth + 1]:
            if wordsearch_dfs_helper_lowmem(board, word, candidaterow, candidatecol, depth + 1):
                result = True
                break
    board[rowidx][colidx] = word[depth]
    return result


if __name__ == '__main__':
    print(wordsearch_recursive([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
