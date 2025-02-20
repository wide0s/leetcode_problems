/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode *prev, *curr, *temp;

    if (head && head->next) {
        prev = head;
        curr = head->next;
        while (curr) {
            if (curr->val == prev->val) {
                prev->next = curr->next;
                temp = curr;
                curr = curr->next;
                free(temp);
            } else {
                prev = curr;
                curr = curr->next;
            }
        }
    }
    return head;
}
