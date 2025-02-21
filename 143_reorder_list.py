# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import listnodes, nodestolist

class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
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
        # move slow pointer to the middle of the list
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half of the list
        head2 = reverse(slow.next)
        # now the slow pointer points to the tail
        slow.next = None
        # reorder the list by iterating over the second
        # half; the second half always has less or equal
        # number of nodes as the first half
        slow = head
        while head2 is not None:
            slow_next = slow.next
            slow.next = head2
            head2_next = head2.next
            head2.next = slow_next
            slow = slow_next
            head2 = head2_next

vectors = [
        [1], [1],
        [1,2], [1,2],
        [1,2,3], [1,3,2],
        [1,2,3,4], [1,4,2,3],
        [1,2,3,4,5], [1,5,2,4,3]
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    print(a)
    head = listnodes([x for x in a])
    expected = vectors[i + 1]
    Solution().reorderList(head)
    returned = nodestolist(head)
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'
