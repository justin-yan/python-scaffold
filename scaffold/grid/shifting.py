from itertools import chain
from typing import List


# https://leetcode.com/problems/shift-2d-grid/
def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:
    # Use divmod to calculate an initial offset.
    # Walk the matrix and slot elements into place following the shifting rules
    height = len(grid)
    width = len(grid[0])
    mat = [[-2000 for i in range(width)] for j in range(height)]

    prelimrowinc, columnincrement = divmod(k, width)
    throwaway, rowincrement = divmod(prelimrowinc, height)
    for rowidx, row in enumerate(grid):
        for colidx, element in enumerate(row):
            mat[rowincrement][columnincrement] = element
            columnincrement = (columnincrement + 1) % width
            if columnincrement == 0:
                rowincrement = (rowincrement + 1) % height
    return mat

    # A simpler solution involves stacking the entire matrix into a long list
    # rotating it, and then reconstituting the matrix
    # flatmat = chain.from_iterable(mat)
    flatmat = [el for row in grid for el in row] * 2
    offset = k % (height * width)
    retlist = flatmat[(height * width - offset):(2 * height * width - offset)]
    # Another way to do this is to not double it
    # flatmat = [el for row in grid for el in row]
    # Then concatenate two slices, prepending the last offset numbers (which start the new matrix)
    # retlist = flatmat[-offset:] + flatmat[:-offset]
    return [retlist[rowidx * width:(rowidx + 1) * width] for rowidx in range(height)]
    # Another way to do this is to use a range incrementor
    # return [retlist[idx:idx + width] for idx in range(0, width * height, width)]
