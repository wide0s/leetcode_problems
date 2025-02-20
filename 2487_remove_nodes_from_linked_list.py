# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import listnodes, nodestolist

class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        def reverse(head):
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
        head = reverse(head)
        max_val = head.val
        prev, node = head, head
        while node is not None:
            if node.val < max_val:
                prev.next = node.next
                # free(node)
            else:
                max_val = node.val
                prev = node
            node = prev.next # same as node.next
        return reverse(head)

vectors = [
        [5,2,13,3,8], [13,8],
        [1,1,1,1], [1,1,1,1]
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    print(a)
    head = listnodes(a)
    expected = vectors[i + 1]
    returned = Solution().removeNodes(head)
    returned = nodestolist(returned)
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'
