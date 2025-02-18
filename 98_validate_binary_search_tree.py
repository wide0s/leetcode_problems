# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binarytree import buildtree, inorder_tree_print

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def inorder_traversal(root, keys=None):
            if keys is None:
                keys = []
            if root is not None:
                inorder_traversal(root.left, keys)
                keys.append(root.val)
                inorder_traversal(root.right, keys)
            return keys
        a = inorder_traversal(root)
        for i in range(len(a) - 1):
            if a[i] >= a[i + 1]:
                return False
        return True

vectors = [
        [1], True,
        [2,1,3], True,
        [5,1,4,None,None,3,6], False,
        [2,2,2], False
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    expected = vectors[i+1]
    tree = buildtree(a)
    print(f'{a}, {expected}')
    inorder_tree_print(tree)
    print('')
    returned = Solution().isValidBST(tree)
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'
