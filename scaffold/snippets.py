from collections import defaultdict
from queue import PriorityQueue


def twodimarray(rows, columns):
    # Access via mat[row][column]
    nrows = rows
    ncols = columns
    mat = [[False for i in range(ncols)] for j in range(nrows)]
    return mat

if __name__ == '__main__':
    # Single-pass test cases
    test_cases = [
        ([1, 2], "output"),
        (["arg1", "arg2"], "output")
    ]

    for case in test_cases:
        input, output = case
        result = twodimarray(*input)
        assert result == output, "input: {}, result: {}, desired: {}".format(input, result, output)

    # Multi-invocation test cases
    test_cases = [
        [
            ([1, 2], "output"),
            (["arg1", "arg2"], "output")
        ],
        [
            ([1, 2], "output"),
            (["arg1", "arg2"], "output")
        ]
    ]

    for case in test_cases:
        for invocation in case:
            input, output = invocation
            result = twodimarray(*input)
            assert result == output, "input: {}, result: {}, desired: {}".format(input, result, output)
