#include <stdlib.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* removeElements(struct ListNode* head, int val) {
    struct ListNode *root;
    struct ListNode *node;
    struct ListNode *prev;

    if (!head) {
        return NULL;
    }

    root = malloc(sizeof(*root));
    if (!root) {
        return NULL;
    }
    root->val = -1;
    root->next = head;

    prev = root;
    node = root->next;
    while (node) {
        if (node->val == val) {
            prev->next = node->next;
            node->next = NULL;
            free(node);
            node = prev;
        }
        prev = node;
        node = node->next;
    }
    head = root->next;
    free(root);
    return head;
}
