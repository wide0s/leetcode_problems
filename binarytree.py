# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_tree_walk(root, keys=None):
    """
    Returns an array of the keys of a binary tree in order
    with the node value first, then the node.left key,
    and then the node.right key.
    type: TreeNode
    rtype: List[int]
    """
    # empty tree has no keys
    if root is None:
        return None # TODO: maybe []?
    if keys is None:
        keys = [root.val]
    if root.left is not None or root.right is not None:
        k = root.left.val if root.left is not None else None
        keys.append(k)
        k = root.right.val if root.right is not None else None
        keys.append(k)
        preorder_tree_walk(root.left, keys)
        preorder_tree_walk(root.right, keys)
    return keys

def preorder_tree_print(tree, depth=0):
    if tree is None:
        return
    print(' ' * depth + f'{tree.val}')
    preorder_tree_print(tree.left, depth + 1)
    preorder_tree_print(tree.right, depth + 1)

def postorder_tree_print(tree, depth=0):
    if tree is None:
        return
    postorder_tree_print(tree.left, depth + 1)
    postorder_tree_print(tree.right, depth + 1)
    print(' ' * depth + f'{tree.val}')

def inorder_tree_print(tree, depth=0):
    if tree is None:
        return
    inorder_tree_print(tree.left, depth + 1)
    print(' ' * depth + f'{tree.val}')
    inorder_tree_print(tree.right, depth + 1)

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
    if root is None:
        return True
    # height of left and right sub trees
    lh = tree_height(root.left)
    rh = tree_height(root.right)
    return abs(lh - rh) <= 1 and tree_balanced(root.left) \
                    and tree_balanced(root.right)
