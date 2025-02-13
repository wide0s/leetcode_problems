# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import listnodes, ListNode, nodestolist

class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(0, head)
        prev, node = head, head.next
        while node is not None:
            v = node.val << 1
            if v > 9:
                prev.val += 1
                v %= 10
            node.val = v
            prev, node = node, node.next
        return head if head.val > 0 else head.next


vectors = [
        [0], [0],
        [1], [2],
        [2], [4],
        [3], [6],
        [4], [8],
        [5], [1,0],
        [6], [1,2],
        [7], [1,4],
        [8], [1,6],
        [9], [1,8],
        [1,0], [2,0],
        [1,8,9], [3,7,8],
        [9,9,9], [1,9,9,8],
        [9], [1,8]
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    print(a)
    head = listnodes(a)
    expected = vectors[i+1]
    returned = Solution().doubleIt(head)
    returned = nodestolist(returned)
    assert expected == returned, f'for {a} expected {expected}, but {returned}'
