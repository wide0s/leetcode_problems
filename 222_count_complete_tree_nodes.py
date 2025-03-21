# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binarytree import buildtree, inorder_tree_print

class Solution(object):

    def leftHeight(self, root):
        height = 0
        while root is not None:
            height += 1
            root = root.left
        return height

    def rightHeight(self, root):
        height = 0
        while root is not None:
            height += 1
            root = root.right
        return height

    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        # optimization
        lh = self.leftHeight(root)
        rh = self.rightHeight(root)
        if lh == rh:
            return 2**lh - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

vectors = [
        None, 0,
        [1], 1,
        [1,2,3,4,5,6], 6,
        [x * pow(-1,x) for x in range(16)], 16
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    expected = vectors[i+1]
    tree = buildtree(a)
    print(f'{a} {expected}')
    inorder_tree_print(tree)
    print('')
    returned = Solution().countNodes(tree)
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'
