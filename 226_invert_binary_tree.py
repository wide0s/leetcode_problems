# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binarytree import TreeNode, preorder_tree_walk

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def bstInvert(root):
            if root is None:
                return
            bstInvert(root.left)
            bstInvert(root.right)
            root.left, root.right = root.right, root.left
        bstInvert(root)
        return root

tree = None
print(tree)
assert Solution().invertTree(tree) is None, f'for None expected None!' 

a = [4,2,7,1,3,6,9]
print(a)
tree = TreeNode(4)
tree.left = TreeNode(2)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right = TreeNode(7)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(9)
expected = [4,7,2,9,6,3,1]
returned = preorder_tree_walk(Solution().invertTree(tree))
assert returned == expected, f'for {a} expected {expected}, but returned {returned}!'

a = [2,1,3]
print(a)
tree = TreeNode(2)
tree.left = TreeNode(1)
tree.right = TreeNode(3)
expected = [2,3,1]
returned = preorder_tree_walk(Solution().invertTree(tree))
assert returned == expected, f'for {a} expected {expected}, but returned {returned}!'
