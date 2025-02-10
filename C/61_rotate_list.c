struct ListNode {
	int val;
	struct ListNode *next;
}

struct ListNode* rotateRight(struct ListNode* head, int k) {
        struct ListNode *tail, *prev;
        unsigned rotations, i, n = 1;

        /* sanity check */
        if (!head || k < 1)
            return head;

        /* look for the tail node and calculate the 
           length (n) of the list */
        tail = head;
        while (tail->next) {
            tail = tail->next;
            n += 1;
        }

        /* find the actual min number of rotations */
        rotations = k % n;
        if (!rotations)
            return head;

        /* close the list into the ring and rotate the list
           starting from the tail */
        tail->next = head;
        prev = tail;
        for (i = 0; i < n - rotations + 1; ++i) {
            prev = tail;
            tail = tail->next;
        }

        /* open the ring list */
        prev->next = NULL;
        return tail;
}
