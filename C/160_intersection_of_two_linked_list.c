/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
static size_t length(const struct ListNode* head) {
    size_t sz = 0;
    while (head) {
        head = head->next;
        sz++;
    }
    return sz;
}

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode *temp;
    size_t lenA, lenB, n_skip = 0;

    if (!headA || !headB)
        return NULL;
    lenA = length(headA);
    lenB = length(headB);
    n_skip = lenA - lenB;
    if (lenB > lenA) {
        temp = headA;
        headA = headB;
        headB = temp;
        n_skip = lenB - lenA;
    }

    while (n_skip-- > 0)
        headA = headA->next;

    while (headA) {
        if (headA == headB)
            return headA;
        headA = headA->next;
        headB = headB->next;
    }
    return NULL;
}
