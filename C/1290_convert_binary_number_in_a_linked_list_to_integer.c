/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int getDecimalValue(struct ListNode* head) {
    int d = 0;

    if (head) {
        while (head) {
            d = (d << 1) + head->val;
            head = head->next;
        }
    }
    return d;
}
