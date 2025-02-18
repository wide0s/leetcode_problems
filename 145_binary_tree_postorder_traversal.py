# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binarytree import buildtree, postorder_tree_print

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def postorder_traversal(root, keys=[]):
            if root is not None:
                postorder_traversal(root.left, keys)
                postorder_traversal(root.right, keys)
                keys.append(root.val)
            return keys
        return postorder_traversal(root)

vectors = [
        None, [],
        [1], [1],
        [1,None,2,3], [3,2,1],
        [1,2,3,4,5,None,8,None,None,6,7,9], [4,6,7,5,2,9,8,3,1]
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    expected = vectors[i+1]
    tree = buildtree(a)
    print(a)
    postorder_tree_print(tree)
    print('')
    returned = Solution().postorderTraversal(tree)
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'
