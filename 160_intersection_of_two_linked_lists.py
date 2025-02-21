# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from linkedlist import listnodes, nodestolist

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        def length(head):
            n = 0
            while head is not None:
                n += 1
                head = head.next;
            return n
        lenA = length(headA)
        lenB = length(headB)
        skip_nodes = abs(lenA - lenB)
        if lenB > lenA:
            headA, headB = headB, headA
        while skip_nodes > 0:
            skip_nodes -= 1
            headA = headA.next
        while headA is not None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

vectors = [
        [4,1,8,4,5], 8, [5,6,1],
        [1,9,1,2,4], 2, [3],
        [2,6,4], None, [1,5],
        [1], None, [2],
        [1,2,3,4,5,6,7,8,9,10,11,12,13], 10, [99,87,56,-3],
        ]

for i in range(0, len(vectors), 3):
    a = vectors[i]
    intersectVal = vectors[i + 1]
    b = vectors[i + 2]
    headA = listnodes(a)
    headB = listnodes(b)
    tailB = headB
    while tailB.next is not None:
        tailB = tailB.next
    intersectNode = headA
    while intersectNode is not None and intersectNode.val != intersectVal:
        intersectNode = intersectNode.next
    tailB.next = intersectNode
    print(f'{a} and {nodestolist(headB)} intersects at {intersectVal}')
    returned = Solution().getIntersectionNode(headA, headB)
    assert intersectNode == returned, f'for {a} expected {intersectVal}, but returned {returned.val if returned is not None else None}!'
