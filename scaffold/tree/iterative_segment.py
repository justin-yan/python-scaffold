class IterativeSegment:
    """
    This implementation should work for any Monoid.  Specifically, we require:

    - Associativity
    - A two-sided identity
    """
    def __init__(self, init_array, fn=lambda x, y: x + y, fn_identity=0):
        self.agg = fn
        self.identity = fn_identity
        arrleng = len(init_array)
        pow = 1
        while pow < arrleng:
            pow *= 2
        self.length = pow
        self.tree = [fn_identity] * (2 * self.length)
        self.__init_tree(init_array)

    def __init_tree(self, arr):
        """
        The idea of the segment tree implicitly stored in an array vs. using nodes and recursion is to use bit-twiddling
        to quickly iteratively index to each range.

        It's easiest to imagine for a full binary tree:

        Given [1,2,3,4], we set up:
        [0,0,0,0,0,0,0,0]
        We then put each of the initial values at the end of the tree array:
        [0,0,0,0,1,2,3,4]
        Now, the idea is that elements 3 and 4 need to have their sum represented:
        [0,0,0,7,1,2,3,4]
        [0,0,3,7,1,2,3,4]
        [0,10,3,7,1,2,3,4]
        000 => root
        001 => 0 - 4
        010 => 0 - 2
        011 => 2 - 4
        100 => 0
        101 => 1
        110 => 2
        111 => 3

        starting the tree at 1-index is easier, since that allows regular integer division to determine the parent relationship.
        In effect, the location of the first significant bit determines how wide of a segment the node represents
        And the remaining bits determines which segment is covered.

        For an array that isn't a perfect power of 2, the easiest thing to do is to just extend the array to be the next power of 2.

        This implementation will work for a known *upfront* array size, but does not handle resizing, etc.

        """
        for i in range(self.length):
            try:
                lval = arr[i]
            except IndexError as e:
                lval = self.identity
            self.tree[self.length + i] = lval
        for i in range(self.length - 1, 0, -1):
            self.tree[i] = self.agg(self.tree[2 * i], self.tree[2 * i + 1])

    def update_tree(self, idx, value):
        i = idx + self.length
        self.tree[i] = value
        while i > 1:
            parent = i // 2
            self.tree[parent] = self.agg(self.tree[2 * parent], self.tree[2 * parent + 1])
            i = parent

    # Calculates range query on 0-indexed base array, including left, excluding right.
    def query_tree(self, left, right):
        lacc = self.identity
        racc = self.identity
        left += self.length
        right += self.length
        # The idea of the interior loop is to determine whether the node is the left or right child.
        while left < right:
            if (left & 1):
                # If you are the right child, you must be included, and then we want to go to the right of the parent
                lacc = self.agg(lacc, self.tree[left])
                left += 1
            if (right & 1):
                # If you are the right child, because we are *exclusive* on the right boundary, we want to include the left
                # and then go to the left of the parent.
                right -= 1
                racc = self.agg(self.tree[right], racc)
            left = left // 2
            right = right // 2
        return self.agg(lacc, racc)

class RangeMinQ(IterativeSegment):
    def __init__(self, init_array):
        super().__init__(init_array, lambda x, y: min(x, y), 9223372036854775807)

class RangeMaxQ(IterativeSegment):
    def __init__(self, init_array):
        super().__init__(init_array, lambda x, y: max(x, y), -9223372036854775807)

class Substring(IterativeSegment):
    def __init__(self, init_array):
        super().__init__(init_array, lambda x, y: x + y, "")

class LeftAnnihilator(IterativeSegment):
    """
    This doesn't work properly because of the lack of a two-sided identity, despite it being an associative operation.
    """
    def __init__(self, init_array):
        super().__init__(init_array, lambda x, y: x, 0)


if __name__ == "__main__":
    init_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    s = IterativeSegment(init_array)
    print(s.tree)
    print(s.query_tree(2, 10))

    rmq = RangeMinQ(init_array)
    print(rmq.tree)
    print(rmq.query_tree(2,10))

    rmq = RangeMaxQ(init_array)
    print(rmq.tree)
    print(rmq.query_tree(2,10))

    init_array = "TRYTHISSTRING"
    s = Substring(init_array)
    print(s.tree)
    print(s.query_tree(2,10))
