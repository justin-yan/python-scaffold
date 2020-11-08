from typing import Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: TreeNode) -> int:
    return diameterHelper(root)[0]

def diameterHelper(node: TreeNode) -> Tuple[int, int]:
    if not node:
        return (0, 0)

    ldi, lh = diameterHelper(node.left)
    rdi, rh = diameterHelper(node.right)

    newdiameter = max(ldi, rdi, lh + rh)  # Diameter is the *path* length, which just combines the left and right height
    newheight = max(lh, rh) + 1  # Height is the number of *nodes* including the root.
    return (newdiameter, newheight)
