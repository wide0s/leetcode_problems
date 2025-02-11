# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import listnodes, nodestolist

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        assert head is not None
        n = 0
        while head is not None:
            n = (n << 1) + head.val
            head = head.next
        return n

vectors = [
        [0], 0,
        [1], 1,
        [1,0], 2,
        [1,1], 3,
        [1,0,0], 4,
        [1,0,1], 5,
        [1,1,0], 6,
        [1,1,1], 7,
        [1,0,0,0], 8,
        [1,0,0,1], 9,
        [1,0,1,0], 10
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    print(a)
    expected = vectors[i+1]
    head = listnodes(a)
    returned = Solution().getDecimalValue(head)
    assert returned == expected, f'for {a} expected {expected}, but returned {returned}!'
