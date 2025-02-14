/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

static struct ListNode* allocNode(int val, struct ListNode *next) {
    struct ListNode *node;

    node = malloc(sizeof(*node));
    if (node) {
        node->val = val;
        node->next = next;
    }
    return node;
}

struct ListNode* doubleIt(struct ListNode* head) {
    struct ListNode *prev, *node;
    int v;

    if (!head)
        return head;

    node = allocNode(0, head);
    /* TODO: here we changing the head of the given list
     * which is error prone as a caller may rely on exiting
     * pointer. The gentle approach would be to swap head
     * with next and values in (2) and return original head
     * pointer. */
    if (node) {
        head = node;
        prev = head;
        node = head->next;
        while (node) {
            v = node->val << 1;
            if (v > 9) {
                prev->val++;
                v %= 10;
            }
            node->val = v;
            prev = node;
            node = node->next;
        }
        if (!head->val) { /* (2) */
            node = head;
            head = head->next;
            free(node);
        }
    }
    return head;
}
