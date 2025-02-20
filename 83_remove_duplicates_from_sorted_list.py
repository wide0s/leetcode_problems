# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import listnodes, nodestolist

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        prev, node = head, head.next
        while node is not None:
            if node.val == prev.val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return head

vectors = [
        None, None,
        [1], [1],
        [1,1,2], [1,2],
        [1,1,2,3,3], [1,2,3]
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    print(a)
    expected = vectors[i + 1]
    returned = Solution().deleteDuplicates(listnodes(a))
    returned = nodestolist(returned)
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'
