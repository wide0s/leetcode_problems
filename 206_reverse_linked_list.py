# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import listnodes, nodestolist, printnodes

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        prev, node = head, head.next
        head.next = None
        while node.next is not None:
            next_node = node.next
            node.next = prev
            prev, node = node, next_node
        node.next = prev
        return node

vectors = [
        [1], [1],
        [1,2], [2,1],
        [1,2,3], [3,2,1],
        [1,2,3,4], [4,3,2,1],
        [1,2,3,4,5], [5,4,3,2,1],
        ]

assert Solution().reverseList(None) is None, f'for None expected None!'

for i in range(0, len(vectors), 2):
    a = vectors[i]
    print(a)
    head = listnodes(a)
    expected = vectors[i+1]
    returned = Solution().reverseList(head)
    returned = nodestolist(returned)
    assert returned == expected, f'for {a} expected {expected}, but returned {returned}!'
