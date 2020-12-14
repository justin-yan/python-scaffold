class DSU:
    """
    Implementing a disjoint-set union structure.
    """

    def __init__(self, n):
        self.pointer_array = list(range(n))
        self.sizes = [1] * n

    def find(self, p):
        while p != self.pointer_array[p]:
            twohop = self.pointer_array[self.pointer_array[p]]
            self.pointer_array[p] = twohop  # compress
            p = twohop
        return p

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return

        if self.sizes[p_root] < self.sizes[q_root]:
            self.pointer_array[p_root] = q_root
            self.sizes[q_root] += self.sizes[p_root]
        else:
            self.pointer_array[q_root] = p_root
            self.sizes[p_root] += self.sizes[q_root]
