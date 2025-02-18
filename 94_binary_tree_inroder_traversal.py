# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binarytree import buildtree, inorder_tree_print

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

vectors = [
        None, [],
        [1], [1],
        [1,None,2,3], [1,3,2],
        [1,2,3,4,5,None,8,None,None,6,7,9], [4,2,6,5,7,1,3,9,8]
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    expected = vectors[i+1]
    tree = buildtree(a)
    print(a)
    inorder_tree_print(tree)
    print('')
    returned = Solution().inorderTraversal(tree)
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'
