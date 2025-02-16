/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
static void __invertTree(struct TreeNode *root) {
    struct TreeNode *tmp;

    if (root) {
        __invertTree(root->left);
        __invertTree(root->right);
        tmp = root->left;
        root->left = root->right;
        root->right = tmp;
    }
}

struct TreeNode* invertTree(struct TreeNode *root) {
    __invertTree(root);
    return root;
}
