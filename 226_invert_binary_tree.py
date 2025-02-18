# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binarytree import buildtree, is_same_tree, inorder_tree_print

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

vectors = [
        None, None,
        [4,2,7,1,3,6,9], [4,7,2,9,6,3,1],
        [2,1,3], [2,3,1]
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    b = vectors[i+1]
    tree = buildtree(a)
    expected = buildtree(b)
    print(f'{a} {b}')
    inorder_tree_print(tree)
    print('- %< -')
    inorder_tree_print(expected)
    print('')
    returned = Solution().invertTree(tree)
    assert is_same_tree(returned, expected), f'for {a} expected {expected}, but returned {returned}!'
