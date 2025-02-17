# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binarytree import TreeNode

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def inorder_traversal(root, keys=[]):
            if root is not None:
                inorder_traversal(root.left, keys)
                keys.append(root.val)
                inorder_traversal(root.right, keys)
            return keys
        return inorder_traversal(root)

a = None
expected = []
returned = Solution().inorderTraversal(a)
assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'

a = [1]
tree = TreeNode(1)
expected = [1]
returned = Solution().inorderTraversal(tree)
assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'

a = [1,None,2,3]
tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)
expected = [1,3,2]
returned = Solution().inorderTraversal(tree)
assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'

a = [1,2,3,4,5,None,8,None,None,6,7,9]
tree = TreeNode(1)
tree.right = TreeNode(3)
tree.right.right = TreeNode(8)
tree.right.right.left = TreeNode(9)
tree.left = TreeNode(2)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.left.right.left = TreeNode(6)
tree.left.right.right = TreeNode(7)
expected = [4,2,6,5,7,1,3,9,8]
returned = Solution().inorderTraversal(tree)
assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'
