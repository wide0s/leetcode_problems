/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapNodes(struct ListNode* head, int k) {
    struct ListNode *first, *second, *temp;

    if (!head || k < 1)
        return NULL;
    first = head;
    for (int i = 1; i < k; i++) {
        if (first->next)
            first = first->next;
    }
    second = head;
    temp = first;
    while (temp->next) {
        temp = temp->next;
        second = second->next;
    }
    k = first->val;
    first->val = second->val;
    second->val = k;
    return head;
}
