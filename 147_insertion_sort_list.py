# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import ListNode, listnodes, nodestolist


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        head = ListNode(0, head)
        prev = head.next
        node = head.next.next
        while node is not None:
            if node.val > prev.val:
                prev = prev.next
                node = node.next
                continue
            temp = head
            while node.val > temp.next.val:
                temp = temp.next
            prev.next = node.next
            node.next = temp.next
            temp.next = node
            node = prev.next
        return head.next

vectors = [
        [4,2,1,3], [1,2,3,4],
        [-1,5,3,4,0], [-1,0,3,4,5]
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    print(a)
    head = listnodes(a)
    expected = vectors[i + 1]
    returned = Solution().insertionSortList(head)
    returned = nodestolist(returned)
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'
