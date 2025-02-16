# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binarytree import TreeNode, preorder_tree_walk

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        def tree_insert(root, val):
            new = TreeNode(val)
            if root is None:
                return new
            parent = None
            current = root
            while current is not None:
                parent = current
                if current.val > new.val:
                    current = current.left
                elif current.val < new.val:
                    current = current.right
                else:
                    return root
            if parent.val > new.val:
                parent.left = new
            else:
                parent.right = new
            return root
        root = None
        for i in range(0, len(preorder)):
            root = tree_insert(root, preorder[i])
        return root

vectors = [
        [8,5,1,7,10,12], [8,5,10,1,7,None,12],
        [1,3], [1,None,3]
        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    print(nums)
    expected = vectors[i+1]
    returned = Solution().bstFromPreorder(nums)
    a = preorder_tree_walk(returned)
    assert expected == a, f'for {nums} expected {expected}, but returned {a}!'
