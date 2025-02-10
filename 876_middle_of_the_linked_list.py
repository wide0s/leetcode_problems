# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import listnodes, ListNode

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

vectors = [
        [1], 1,
        [1,2], 2,
        [1,2,3], 2,
        [1,2,3,4,5], 3,
        [1,2,3,4,5,6], 4,
        [1,2,3,4,5,6,7], 4,
        [1,2,3,4,5,6,7,8], 5
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    print(f'{a}')
    expected = vectors[i+1]
    head = listnodes(a)
    returned = Solution().middleNode(head).val
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}'
