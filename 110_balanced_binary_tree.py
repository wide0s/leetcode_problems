# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binarytree import buildtree, inorder_tree_print

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

vectors = [
        [3,9,20,None,None,15,7], True,
        [1,2,2,3,3,None,None,4,4], False
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    expected = vectors[i+1]
    tree = buildtree(a)
    print(a)
    inorder_tree_print(tree)
    print('')
    returned = Solution().isBalanced(tree)
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'
