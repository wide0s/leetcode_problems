# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binarytree import buildtree, inorder_tree_print

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

vectors = [
        [1], ['1'],
        [1,2,3,None,5], ['1->2->5','1->3']
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    expected = vectors[i+1]
    tree = buildtree(a)
    print(a)
    inorder_tree_print(tree)
    print('')
    returned = Solution().binaryTreePaths(tree)
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'
