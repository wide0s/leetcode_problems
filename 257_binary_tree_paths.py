# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binarytree import TreeNode, preorder_tree_walk, inorder_tree_print

# NOT MY SOLUTION, https://walkccc.me/LeetCode/problems/257/#__tabbed_1_3
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if root is None:
            return root

        def tree_paths(root, path, pathes):
            if root is None:
                return

            # reached leaf node add path to the pathes
            if root.left is None and root.right is None:
                paths.append(''.join(path) + str(root.val))
                return

            path.append(str(root.val) + '->')
            tree_paths(root.left, path, paths)
            tree_paths(root.right, path, paths)
            path.pop()

        paths = []
        tree_paths(root, [], paths)
        return paths

a = [1]
print(a)
expected = ["1"]
tree = TreeNode(1)
returned = Solution().binaryTreePaths(tree)
assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'

a = [1,2,3,None,5]
print(a)
expected = ["1->2->5","1->3"]
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.right = TreeNode(5)
returned = Solution().binaryTreePaths(tree)
assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'
