# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import listnodes

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None or k < 1:
            return head
        # look for the tail node and calculate the
        # length (n) of the list
        n, tail = 1, head
        while tail.next is not None:
            tail = tail.next
            n += 1
        rotations = k % n
        if rotations == 0:
            return head
        # close the list into the ring
        tail.next = head
        # rotate the list starting from the tail node
        node = tail
        for i in range(n - rotations + 1):
            node, tail = tail, tail.next
        # open the ring list
        node.next = None
        return tail

vectors = [
        [1], 0, [1],
        [1], 1, [1],
        [1, 2, 3, 4, 5], 1, [5, 1, 2, 3, 4],
        [1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3],
        [1, 2, 3, 4, 5], 3, [3, 4, 5, 1, 2],
        [1, 2, 3, 4, 5], 4, [2, 3, 4, 5, 1],
        [1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5],
        [0, 1, 2], 1, [2, 0, 1],
        [0, 1, 2], 2, [1, 2, 0],
        [0, 1, 2], 3, [0, 1, 2]
        ]

for i in range(0, len(vectors), 3):
    a = vectors[i]
    k = vectors[i+1]
    print(f'{a}, k={k}')
    expected = vectors[i+2]
    head1 = listnodes(a)
    head2 = Solution().rotateRight(head1, k)
    if head2 is not None:
        assert type(head1) == type(head2), f'returned {type(head2)} != expected type {type(head1)}!'
    node = head2
    b = None
    while node is not None:
        if b is None:
            b = [node.val]
        else:
            b += [node.val]
        node = node.next
    assert expected == b, f'for {a} expected {expected}, but returned {b}'
