/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
static struct ListNode *allocNode(int val, struct ListNode *next) {
    struct ListNode *node;

    node = malloc(sizeof(*node));
    if (node) {
        node->val = val;
        node->next = next;
    }
    return node;
}

struct ListNode* insertionSortList(struct ListNode* head) {
    struct ListNode *prev, *node, *temp;

    if (!head || !head->next)
        return head;
    head = allocNode(0xdeadbeaf, head);
    if (!head)
        return NULL;
    prev = head->next;
    node = head->next->next;
    while (node) {
        if (node->val > prev->val) {
            prev = prev->next;
            node = node->next;
            continue;
        }
        temp = head;
        while (node->val > temp->next->val)
            temp = temp->next;
        prev->next = node->next;
        node->next = temp->next;
        temp->next = node;
        node = prev->next;
    }
    return head->next;
}
