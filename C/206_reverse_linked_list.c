/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *prev, *node, *next;

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
