from collections import deque

# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# FROM https://stackoverflow.com/questions/67324135/how-to-construct-a-binary-tree-from-leetcode-values-list
def buildtree(arr):
    """
    Builds a binary tree from LeetCode's tree representation
    using an array of values.

    :type List[int]
    :rtype TreeNode
    """
    if arr is None or len(arr) == 0:
        return None
    parents = deque()
    root = TreeNode(arr[0])
    node = root
    for i in range(1, len(arr)):
        if i % 2 == 1:
            if arr[i] is not None:
                node.left = TreeNode(arr[i])
                parents.append(node.left)
        else:
            if arr[i] is not None:
                node.right = TreeNode(arr[i])
                parents.append(node.right)
            node = parents.popleft()
    return root

# FROM https://dev.to/sibprogrammer/build-binary-tree-from-array-1f5o
def binarytree(arr):
    """
    Builds a binary tree from the standard represetation
    of a binary tree via an array of values. It does not
    work with LeetCode's representation of a binary tree.

    :type List[int]
    :rtype: TreeNode
    """
    if arr is None or len(arr) == 0:
        return None
    def build_tree(a, i, n):
        root = None
        if i < n and a[i] is not None:
            root = TreeNode(a[i])
            root.left = build_tree(a, 2 * i + 1, n)
            root.right = build_tree(a, 2 * i + 2, n)
        return root
    return build_tree(arr, 0, len(arr))

def leetcode_tree_repr(root, keys=None):
    """
    Returns an array of binary tree keys in LeetCode
    representation.

    type: TreeNode
    rtype: List[int]
    """
    # empty tree has no keys
    if root is None:
        return None # TODO: maybe []?
    assert type(root) == TreeNode, f'type(root) must be TreeNode, but it is {type(root)}!'
    if keys is None:
        keys = [root.val]
    if root.left is not None or root.right is not None:
        k = root.left.val if root.left is not None else None
        keys.append(k)
        k = root.right.val if root.right is not None else None
        keys.append(k)
        leetcode_tree_repr(root.left, keys)
        leetcode_tree_repr(root.right, keys)
    return keys

def preorder_tree_traversal(root, keys=None):
    if keys is None:
        keys = [] # returns [] for an empty tree
    if root is not None:
        keys.append(root.val)
        preorder_tree_traversal(root.left, keys)
        preorder_tree_traversal(root.right, keys)
    return keys

def inorder_tree_traversal(root, keys=None):
    if keys is None:
        keys = [] # returns [] for an empty tree
    if root is not None:
        inorder_tree_traversal(root.left, keys)
        keys.append(root.val)
        inorder_tree_traversal(root.right, keys)
    return keys

def postorder_tree_traversal(root, keys=None):
    if keys is None:
        keys = [] # returns [] for an empty tree
    if root is not None:
        postorder_tree_traversal(root.left, keys)
        postorder_tree_traversal(root.right, keys)
        keys.append(root.val)
    return keys

def preorder_tree_print(tree, depth=0):
    if tree is not None:
        print(' ' * depth + f'{tree.val}')
        preorder_tree_print(tree.left, depth + 1)
        preorder_tree_print(tree.right, depth + 1)

def inorder_tree_print(tree, depth=0):
    if tree is not None:
        inorder_tree_print(tree.left, depth + 1)
        print(' ' * depth + f'{tree.val}')
        inorder_tree_print(tree.right, depth + 1)

def postorder_tree_print(tree, depth=0):
    if tree is not None:
        postorder_tree_print(tree.left, depth + 1)
        postorder_tree_print(tree.right, depth + 1)
        print(' ' * depth + f'{tree.val}')

def bstree_search(tree, key):
    """
    Searches for a node with a given key in a binary
    search tree.

    :type TreeNode
    :type int
    :rtype TreeNode
    """
    while tree is not None and key != tree.val:
        if val < tree.key:
            tree = tree.left
        else:
            tree = tree.right
    return tree

def bstree_minimum(tree):
    """
    Returns the node with the minimum value.

    :type TreeNode
    :rtype TypeNode
    """
    while tree.left is not None:
        tree = tree.left
    return tree

def bstree_maximum(tree):
    """
    Returns the node with the maximum value.

    :type TreeNode
    :rtype TypeNode
    """
    while tree.right is not None:
        tree = tree.right
    return tree

def is_same_tree(tree1, tree2):
    """
    Checks if two binary trees are the same.

    type: TreeNode
    type: TreeNode
    rtype: bool
    """
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    return tree1.val == tree2.val and \
            is_same_tree(tree1.left, tree2.left) and \
            is_same_tree(tree1.right, tree2.right)

def tree_size(tree):
    """
    Returns number of keys in tree.

    type: TreeNode
    rtype: int
    """
    # empty tree has 0 keys
    if tree is None:
        return 0
    return 1 + tree_size(tree.left) + tree_size(tree.right)

def tree_height(tree):
    """
    Returns a tree height.

    type: TreeNode
    rtype: int
    """
    # height of empty tree is zero
    if tree is None:
        return 0
    return 1 + max(tree_height(tree.left), tree_height(tree.right))

def tree_balanced(tree):
    """
    Checks if a binary tree is height-balanced tree, i.e. depth of the
    two subtrees of every node never differs by more than one.

    type: TreeNode
    rtype: bool
    """
    # empty tree is balanced
    if tree is None:
        return True
    # height of left and right sub trees
    lh = tree_height(tree.left)
    rh = tree_height(tree.right)
    return abs(lh - rh) <= 1 and tree_balanced(tree.left) \
                    and tree_balanced(tree.right)
