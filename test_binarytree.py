from binarytree import buildtree, tree_height, tree_size, leetcode_tree_repr, tree_balanced, is_same_tree
from binarytree import inorder_tree_traversal, postorder_tree_traversal, preorder_tree_traversal
from binarytree import inorder_tree_print, preorder_tree_print, postorder_tree_print

vectors = [
    'buildtree', [1], None,
    'leetcode_tree_repr', '$tree', [1],
    'tree_size', '$tree', 1,
    'tree_balanced', '$tree', True,
    'tree_height', '$tree', 1,
    'preorder_tree_traversal', '$tree', [1],
    'postorder_tree_traversal', '$tree', [1],
    'inorder_tree_traversal', '$tree',  [1],
    'inorder_tree_print', '$tree', None,
    'preorder_tree_print', '$tree', None,
    'postorder_tree_print', '$tree', None,
    'buildtree', [1,None,2,3], None,
    'leetcode_tree_repr', '$tree', [1,None,2,3,None], #?
    'tree_size', '$tree', 3,
    'preorder_tree_traversal', '$tree', [1,2,3],
    'postorder_tree_traversal', '$tree', [3,2,1],
    'inorder_tree_traversal', '$tree',  [1,3,2],
    'tree_balanced', '$tree', False,
    'tree_height', '$tree', 3,
    'inorder_tree_print', '$tree', None,
    'preorder_tree_print', '$tree', None,
    'postorder_tree_print', '$tree', None,
    'buildtree', [1,2,3,4,5,None,8,None,None,6,7,9], None,
    'leetcode_tree_repr', '$tree', [1,2,3,4,5,6,7,None,8,9,None], #?
    'tree_size', '$tree', 9,
    'preorder_tree_traversal', '$tree', [1,2,4,5,6,7,3,8,9],
    'postorder_tree_traversal', '$tree', [4,6,7,5,2,9,8,3,1],
    'inorder_tree_traversal', '$tree',  [4,2,6,5,7,1,3,9,8],
    'tree_height', '$tree', 4,
    'tree_balanced', '$tree', False,
    'inorder_tree_print', '$tree', None,
    'preorder_tree_print', '$tree', None,
    'postorder_tree_print', '$tree', None,
    'buildtree', [8,3,10,1,6,None,14,None,None,4,7,13], None,
    'leetcode_tree_repr', '$tree', [8,3,10,1,6,4,7,None,14,13,None], #?
    'tree_size', '$tree', 9,
    'preorder_tree_traversal', '$tree', [8,3,1,6,4,7,10,14,13],
    'postorder_tree_traversal', '$tree', [1,4,7,6,3,13,14,10,8],
    'inorder_tree_traversal', '$tree',  [1,3,4,6,7,8,10,13,14],
    'tree_balanced', '$tree', False,
    'inorder_tree_print', '$tree', None,
    'preorder_tree_print', '$tree', None,
    'postorder_tree_print', '$tree', None,
    'buildtree', [], None,
    'tree_balanced', '$tree', True,
    'tree_height', '$tree', 0,
    'inorder_tree_print', '$tree', None,
    'preorder_tree_print', '$tree', None,
    'postorder_tree_print', '$tree', None,
    'buildtree', [3,9,20,None,None,15,7], None,
    'tree_balanced', '$tree', True,
    'tree_height', '$tree', 3,
    'inorder_tree_print', '$tree', None,
    'preorder_tree_print', '$tree', None,
    'postorder_tree_print', '$tree', None,
    'buildtree', [1,2,2,3,3,None,None,4,4], None,
    'tree_balanced', '$tree', False,
    'tree_height', '$tree', 4,
    'inorder_tree_print', '$tree', None,
    'preorder_tree_print', '$tree', None,
    'postorder_tree_print', '$tree', None,
    'buildtree', None, None,
    'buildtree', None, '$tree2',
    'is_same_tree', ['$tree', '$tree2'], True,
    'buildtree', [1], None,
    'buildtree', None, '$tree2',
    'is_same_tree', ['$tree', '$tree2'], False,
    'buildtree', [1,2,2,3,3,None,None,4,4], None,
    'buildtree', [1,2,2,3,3,None,None,4,4], '$tree2',
    'is_same_tree', ['$tree', '$tree2'], True,
    'buildtree', [1,2,2,3,3,None,None,4,4], None,
    'buildtree', [1,2,2,3,3,None,None,5,4], '$tree2',
    'is_same_tree', ['$tree', '$tree2'], False
]

tree = [None, None]
for i in range(0, len(vectors), 3):
    action = vectors[i]
    params = vectors[i + 1]
    if isinstance(params, list):
        resolved_params = []
        for value in params:
            if value == '$tree':
                resolved_params.append(tree[0])
            elif value == '$tree2':
                resolved_params.append(tree[1])
            else:
                resolved_params.append(value)
        params = resolved_params
    elif params == '$tree':
        params = tree[0]
    elif params == '$tree2':
        params = tree[1]
    expected = vectors[i + 2]
    returned = None

    print(f'{action} | {params}, {expected}')
    if action == 'buildtree':
        if expected == '$tree2':
            tree[1] = buildtree(params)
            returned = expected
        else:
            tree[0] = buildtree(params)
    elif action == 'tree_size':
        returned = tree_size(params)
    elif action == 'preorder_tree_traversal':
        returned = preorder_tree_traversal(params)
    elif action == 'postorder_tree_traversal':
        returned = postorder_tree_traversal(params)
    elif action == 'inorder_tree_traversal':
        returned = inorder_tree_traversal(params)
    elif action == 'leetcode_tree_repr':
        returned = leetcode_tree_repr(params)
    elif action == 'tree_balanced':
        returned = tree_balanced(params)
    elif action == 'tree_height':
        returned = tree_height(params)
    elif action == 'inorder_tree_print':
        inorder_tree_print(params)
    elif action == 'preorder_tree_print':
        preorder_tree_print(params)
    elif action == 'postorder_tree_print':
        postorder_tree_print(params)
    elif action == 'is_same_tree':
        returned = is_same_tree(params[0], params[1])
    assert expected == returned, f'expected {expected}, returned {returned}!'
