# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binarytree import buildtree, preorder_tree_print

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def preorder_traversal(root, keys=[]):
            if root is not None:
                keys.append(root.val)
                preorder_traversal(root.left, keys)
                preorder_traversal(root.right, keys)
            return keys
        return preorder_traversal(root)

vectors = [
        None, [],
        [1], [1],
        [1,None,2,3], [1,2,3],
        [1,2,3,4,5,None,8,None,None,6,7,9], [1,2,4,5,6,7,3,8,9]
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    expected = vectors[i+1]
    tree = buildtree(a)
    print(a)
    preorder_tree_print(tree)
    print('')
    returned = Solution().preorderTraversal(tree)
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'
