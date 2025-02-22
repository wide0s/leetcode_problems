/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode *fast, *slow, *prev;
    size_t len, slow_index, unlink_index, skip_nodes;

    if (!head)
        return NULL;
    len = 1;
    prev = NULL;
    slow = head;
    fast = head->next;
    while (fast && fast->next) {
        prev = slow;
        slow = slow->next;
        fast = fast->next->next;
        len += 2;
    }
    if (fast)
        len++;
    slow_index = len / 2 + len % 2 - 1;
    unlink_index = len - n;
    if (unlink_index == 0) {
        fast = head;
        head = head->next;
        free(fast);
    } else if (slow_index == unlink_index) {
        fast = slow;
        prev->next = slow->next;
        free(fast);
    } else {
        skip_nodes = unlink_index - 1;
        if (slow_index < unlink_index)
            skip_nodes -= slow_index;
        else
            slow = head;
        for (int i = 0; i < skip_nodes; i++)
            slow = slow->next;
        fast = slow->next;
        slow->next = slow->next->next;
        free(fast);
    }
    return head;
}
