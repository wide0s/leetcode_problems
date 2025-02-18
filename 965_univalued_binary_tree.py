# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binarytree import buildtree, inorder_tree_print

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def unival_tree(root, val):
            if root is None:
                return True
            if root.val != val:
                return False
            return unival_tree(root.left, val) and unival_tree(root.right, val)
        return unival_tree(root, root.val)

vectors = [
        [1,1,1,1,1,None,1], True,
        [2,2,2,5,2], False
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    expected = vectors[i+1]
    tree = buildtree(a)
    print(a)
    inorder_tree_print(tree)
    print(' ')
    returned = Solution().isUnivalTree(tree)
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'
