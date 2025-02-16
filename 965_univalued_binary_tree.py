# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binarytree import TreeNode

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

a = [1,1,1,1,1,None,1]
expected = True
tree = TreeNode(1)
tree.left = TreeNode(1)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(1)
tree.right = TreeNode(1)
tree.right.right = TreeNode(1)
returned = Solution().isUnivalTree(tree)
assert returned == expected, f'for {a} expected {expected}, but returned {returned}!'

a = [2,2,2,5,2]
expected = False
tree = TreeNode(2)
tree.right = TreeNode(2)
tree.left = TreeNode(2)
tree.left.left = TreeNode(5)
tree.left.right = TreeNode(2)
returned = Solution().isUnivalTree(tree)
assert returned == expected, f'for {a} expected {expected}, but returned {returned}!'
