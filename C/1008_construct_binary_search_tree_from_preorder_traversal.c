/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

static struct TreeNode* allocTreeNode(int val, struct TreeNode *left, struct TreeNode *right) {
    struct TreeNode *node;

    node = malloc(sizeof(*node));
    if (node) {
        node->val = val;
        node->left = left;
        node->right = right;
    }
    return node;
}
#define ALLOC_TREE_NODE(val) allocTreeNode((val), NULL, NULL)

static struct TreeNode* bstInsert(struct TreeNode *root, int val) {
    struct TreeNode *new = ALLOC_TREE_NODE(val);
    struct TreeNode *parent, *current;

    if (!root)
        return new;

    parent = NULL;
    current = root;
    while (current) {
        parent = current;
        if (current->val > new->val) {
            current = current->left;
        } else if (current->val < new->val) {
            current = current->right;
        } else {
            /* should not be here, but... */
            return root;
        }
    }
    if (parent->val > new->val) {
        parent->left = new;
    } else {
        parent->right = new;
    }
    return root;
}

struct TreeNode* bstFromPreorder(int* preorder, int preorderSize) {
    struct TreeNode *root = NULL;
    int i;

    if (preorder && preorderSize) {
        for (i = 0; i < preorderSize; i++) {
            root = bstInsert(root, *preorder);
            preorder++;
        }
    }
    return root;
}
