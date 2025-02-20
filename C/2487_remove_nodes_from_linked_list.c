/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

static struct ListNode* reverseNodes(struct ListNode *head) {
    struct ListNode *prev, *next, *node;

    if (head && head->next) {
        prev = head;
        node = head->next;
        head->next = NULL;
        while (node->next) {
            next = node->next;
            node->next = prev;
            prev = node;
            node = next;
        }
        node->next = prev;
        head = node;
    }
    return head;
}

struct ListNode* removeNodes(struct ListNode* head) {
    struct ListNode *prev, *node;
    int max_val;

    head = reverseNodes(head);
    if (head) {
        prev = head;
        node = head;
        max_val = head->val;
        while (node) {
            if (node->val < max_val) {
                prev->next = node->next;
                free(node);
            } else {
                max_val = node->val;
                prev = node;
            }
            node = prev->next;
        }
    }
    return reverseNodes(head);
}
