/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

static int gcd(int a, int b) {
    while (a > 0 && b > 0) {
        if (a > b) {
            a %= b;
        } else {
            b %= a;
        }
    }
    return a == 0 ? b : a;
}

static struct ListNode* allocNode(int val, struct ListNode *next) {
    struct ListNode *node;

    node = malloc(sizeof(*node));
    if (node) {
        node->val = val;
        node->next = next;
    }
    return node;
}

struct ListNode* insertGreatestCommonDivisors(struct ListNode* head) {
    struct ListNode *node, *prev;

    if (head && head->next) {
        prev = head;
        node = head->next;
        while (node->next) {
            prev->next = allocNode(gcd(prev->val, node->val), prev->next);
            if (!prev->next)
                goto nomem;
            prev = prev->next->next;
            node = node->next;
        }
        prev->next = allocNode(gcd(prev->val, node->val), prev->next);
    }
nomem:
    return head;
}
