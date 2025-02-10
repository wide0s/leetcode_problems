# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import listnodes, ListNode, nodestolist

from math import gcd
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head

        # GCD implementation for Python2
        #
        #def gcd(a, b):
        #    while (a > 0 and b > 0):
        #        if a > b:
        #            a = a % b
        #        else:
        #            b = b % a
        #    return b if a == 0 else a

        prev, node = head, head.next
        while node.next is not None:
            prev.next = ListNode(gcd(prev.val, node.val), prev.next)
            prev = prev.next.next
            node = node.next
        prev.next = ListNode(gcd(prev.val, node.val), prev.next)
        return head

vectors = [
        [18,6,10,3], [18,6,6,2,10,1,3],
        [9,3], [9,3,3],
        [7], [7]
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    print(f'{a}')
    expected = vectors[i+1]
    head = listnodes(a)
    returned = Solution().insertGreatestCommonDivisors(head)
    returned = nodestolist(returned)
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}'
