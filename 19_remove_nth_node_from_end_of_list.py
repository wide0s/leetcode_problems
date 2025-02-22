# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import listnodes, nodestolist

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        length = 1
        prev = None
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            length += 2
        length += 1 if fast is not None else 0
        slow_index = length // 2 + length % 2 - 1
        unlink_index = length - n
        if unlink_index == 0:
            head = head.next
        elif slow_index == unlink_index:
            prev.next = slow.next
        else:
            skip_nodes = unlink_index - 1
            if slow_index < unlink_index:
                skip_nodes -= slow_index
            else:
                slow = head
            for _ in range(skip_nodes):
                slow = slow.next
            slow.next = slow.next.next

        return head

vectors = [
        None, 0, None,
        [1], 1, None,
        [1,2], 1, [1],
        [1,2], 2, [2],
        [1,2,3], 2, [1,3],
        [1,2,3,4], 3, [1,3,4],
        [1,2,3,4,5], 2, [1,2,3,5],
        [1,2,3,4,5,6,7,8], 3, [1,2,3,4,5,7,8],
        [1,2,3,4,5,6,7,8], 5, [1,2,3,5,6,7,8],
        [1,2,3,4,5,6,7,8,9,10], 7, [1,2,3,5,6,7,8,9,10],
        [1,2,3,4,5,6,7,8,9,10,11,12,13], 1, [1,2,3,4,5,6,7,8,9,10,11,12],
        ]

for i in range(0, len(vectors), 3):
    a = vectors[i]
    n = vectors[i+1]
    print(f'{a}, n={n}')
    head = listnodes([ x for x in a ] if a is not None else None)
    expected = vectors[i+2]
    returned = Solution().removeNthFromEnd(head, n)
    returned = nodestolist(returned)
    assert expected == returned, f'for {a} and n {n} expected {expected}, but returned {returned}!'
