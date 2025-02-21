# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import listnodes, nodestolist

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        odd = head
        even_head = head.next
        even = even_head
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


vectors = [
        None, None,
        [1], [1],
        [1,2], [1,2],
        [1,2,3], [1,3,2],
        [1,2,3,4] , [1,3,2,4],
        [1,2,3,4,5], [1,3,5,2,4],
        [2,1,3,5,6,4,7], [2,3,6,7,1,5,4]
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    print(a)
    head = listnodes(a)
    expected = vectors[i + 1]
    returned = nodestolist(Solution().oddEvenList(head))
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'
