# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binarytree import TreeNode, preorder_tree_walk

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True

        def height(root):
            # height of empty tree is zero
            if root is None:
                return 0
            return 1 + max(height(root.left), height(root.right))

        def balanced(root):
            # empty tree is balanced
            if root is None:
                return True
            # height of left and right sub trees
            lh = height(root.left)
            rh = height(root.right)
            return abs(lh - rh) <= 1 and balanced(root.left) \
                    and balanced(root.right)

        return balanced(root)
# None
assert Solution().isBalanced(None), f'for None expected True, but returned False'

# [3,9,20,None,None,15,7]
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)
a = preorder_tree_walk(tree)
print(a)
assert Solution().isBalanced(tree), f'for {a} expected True, but returned False!'

# [1,2,2,3,3,null,null,4,4]
tree = TreeNode(1)
tree.right = TreeNode(2)
tree.left = TreeNode(2)
tree.left.right = TreeNode(3)
tree.left.left = TreeNode(3)
tree.left.left.left = TreeNode(4)
tree.left.left.right = TreeNode(4)
a = preorder_tree_walk(tree)
print(a)
assert not Solution().isBalanced(tree), f'for {a} expected False, but returned True!'

# [1,2,3,4,5,6,null,8]
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right = TreeNode(3)
tree.right.left = TreeNode(6)
tree.right.left.left = TreeNode(8)
a = preorder_tree_walk(tree)
assert not Solution().isBalanced(tree), f'for {a} expected False, but returned True!'
