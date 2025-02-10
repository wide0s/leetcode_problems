# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import listnodes, ListNode, nodestolist

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        if head is not None:
            head = ListNode(None, head)
            prev, node = head, head.next
            while node is not None:
                if node.val == val:
                    prev.next = node.next
                    node.next = None
                    node = prev
                prev, node = node, node.next
            head = head.next
        return head

vectors = [
        [1], 1, None,
        [1,1,1,1], 1, None,
        [1], 0, [1],
        [1,2,6,3,4,5,6], 6, [1,2,3,4,5],
        [7,7,7,7,7,7], 7, None,
        [1,5,5,2,5,3,4,5,6,5,7], 5, [1,2,3,4,6,7],
        ]

for i in range(0, len(vectors), 3):
    a = vectors[i]
    val = vectors[i+1]
    print(f'{a}, val={val}')
    expected = vectors[i+2]
    head1 = listnodes(a)
    returned = Solution().removeElements(head1, val)
    if type(returned) == type(head1):
        returned = nodestolist(returned)
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}'
