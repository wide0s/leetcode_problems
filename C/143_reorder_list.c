/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
static struct ListNode* reverseList(struct ListNode *head) {
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

void reorderList(struct ListNode* head) {
    struct ListNode *fast, *slow, *head2;
    struct ListNode *slow_next, *head2_next;

    if (!head || !head->next)
        return;
    /* 1. move slow pointer to the middle of the list */
    slow = head;
    fast = head->next;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    /* 2. reverse the second half of the list */
    head2 = reverseList(slow->next);
    /* 3. make the middle node a tail of the list */
    slow->next = NULL;
    /* 4. reorder the list by iterating over the
          second half which is safe because it always
          has less or equal number of nodes as the
          first half */
    slow = head;
    while (head2) {
        slow_next = slow->next;
        slow->next = head2;
        head2_next = head2->next;
        head2->next = slow_next;
        slow = slow_next;
        head2 = head2_next;
    }
}
