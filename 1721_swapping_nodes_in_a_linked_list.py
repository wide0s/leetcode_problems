# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import listnodes, nodestolist

class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None or k < 1:
            return None
        first = head
        for _ in range(1, k):
            if first.next is not None:
                first = first.next
        second = head
        temp = first
        while temp.next is not None:
            temp = temp.next
            second = second.next
        first.val, second.val = second.val, first.val
        return head

vectors = [
        None, 0, None,
        [1,2,3,4,5], 1, [5,2,3,4,1],
        [1,2,3,4,5], 2, [1,4,3,2,5],
        [1,2,3,4,5], 3, [1,2,3,4,5],
        [1,2,3,4,5], 4, [1,4,3,2,5],
        [1,2,3,4,5], 5, [5,2,3,4,1],
        [1,2,3,4,5], 10, [5,2,3,4,1],
        [7,9,6,6,7,8,3,0,9,5], 5, [7,9,6,6,8,7,3,0,9,5],
        [1,2,3,4,5,6,7,8,9,10], 3, [1,2,8,4,5,6,7,3,9,10],
        ]

for i in range(0, len(vectors), 3):
    a = vectors[i]
    k = vectors[i+1]
    print(f'\n{a}, k={k}')
    head = listnodes([ x for x in a ] if a is not None else None)
    expected = vectors[i + 2]
    returned = Solution().swapNodes(head, k)
    returned = nodestolist(returned)
    assert expected == returned, f'for {a} and k = {k} expected {expected}, but returned {returned}!'
