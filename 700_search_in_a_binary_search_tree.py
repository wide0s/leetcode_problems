# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binarytree import buildtree, is_same_tree, leetcode_tree_repr, \
        inorder_tree_print

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        def bstree_search(root, val):
            while root is not None and val != root.val:
                if val < root.val:
                    root = root.left
                else:
                    root = root.right
            return root
        return bstree_search(root, val)

vectors = [
        [4,2,7,1,3], 2, [2,1,3],
        [4,2,7,1,2], 5, []
        ]

for i in range(0, len(vectors), 3):
    a = vectors[i]
    val = vectors[i + 1]
    b = vectors[i + 2]
    tree = buildtree(a)
    print(a)
    inorder_tree_print(tree)
    print('')
    expected = buildtree(b)
    returned = Solution().searchBST(tree, val)
    c = leetcode_tree_repr(returned)
    assert is_same_tree(expected, returned), f'for {a} and {val} expected {b}, but returned {c}!'
