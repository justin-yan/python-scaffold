class Fenwick:
    """ https://en.wikipedia.org/wiki/Fenwick_tree
    add: O(logn)
    rangesum: O(logn)

    Given an array of length N, that is 1-indexed, we construct a tree with N+1 elements, with a root of 0 that contains nothing
    Each array element is converted to its binary representation, and is the child of whichever node is represented by removing its least significant 1-bit.
    E.g. 11 (8 + 2 + 1) = 1011 => 1010 => 10 is the parent.

    The value of each node is the range sum starting after its parent up to and including itself:

    Consider the array: [1,2,3,4,5,6,7,8,9]

    0 -> 4 -> 5 is one branch of the tree.

    Node 4 has a value of 10 (prefix sum from 1 to 4)
    Node 5 has a value of 5 (prefix sum from 5 to 5)

    More generally, given the binary representation of a number:

    19 -> 10011

    This number also needs to be part of the prefix range sum stored at any node responsible for capturing it:

    20 ->  10100
    24 ->  11000
    32 -> 100000

    From a heuristic perspective, these are progressively identified by repeatedly adding the least significant bit:

    19 -> 10011
    20 -> 10100 (responsible for 17-20)
    24 -> 11000 (responsible for 17-24)

    This works because you can think of any "1-bit" as indicating a range sum stored in a node in the tree:
    31 -> 11111 means the first node stores 1-16, then the second stores 17-24, then the third 25-28, then the fourth 29-30, and the last 31

    We *subtract* the least significant bit to find the parent (19 - 1 = 18)
    *Adding* the least significant bit, however, breaks out of the subtree to find the next range the index is present in.

    10001 => 10010
    10010 => 10100
    11011 => 11100

    Typically, a Fenwick tree is stored in array which allows for O(1) indexing directly to the element,
    with the tree structure implicit in the relationship between the cells.

    A rangesum is computed in the following way:
        - Given the range (say, 2 - 7), we want to compute (0 - 7) and (0 - 1) and subtract them.
        - For 0-7, we index directly into the array at 7, and accumulate it into a counter.
        - We then go to 7's parent (6), and add it to the same counter.
        - We then go to 6's parent (4), and add it to the counter.
        - Finally, we arrive at 0, which indicates we are done, and we return the value of the counter.

    Adding/mutating and appending an element are effectively the same
        - Say we want to append 10 (add 10 to position 10)
        - update the element itself
        - add the least significant bit to the element itself
        - repeat until the target index update exceeds the size of the tree

    TODO: This assumes fixed-size
    TODO: Support other associative binary operators
    TODO: Support range-sums
    TODO: Should we just assume the input array is 1-indexed and skip the confusing idx translation?
    """
    def __init__(self, size):
        self.arr = [0] * (size + 1)
        self.size = size

    def add(self, index, value):
        internal_index = index + 1  # Fenwick tree storage assumes 1-indexed array
        while internal_index <= self.size + 1:
            self.arr[internal_index] += value
            internal_index += internal_index & -internal_index

    def prefix_sum(self, index):
        internal_index = index + 1
        accumulator = 0
        while internal_index > 0:
            accumulator += self.arr[internal_index]
            internal_index -= internal_index & -internal_index
        return accumulator



if __name__ == "__main__":
    f = Fenwick(10)
    f.add(0, 1)
    f.add(1, 2)
    f.add(2, 3)
    f.add(3, 4)
    f.add(4, 5)
    f.add(5, 6)
    f.add(6, 7)
    f.add(7, 8)
    f.add(8, 9)
    f.add(9, 10)

    print(f.prefix_sum(5))
