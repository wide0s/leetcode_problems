# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import listnodes, nodestolist

class Solution(object):
    # Runtime complexity: O(n)
    # Space complexity: O(n)
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head.next is None:
            return True
        stack = [head.val]
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            stack.append(slow.val)
        if fast is None:
            # the list has odd length and the
            # slow pointer points to the middle
            # node, which has no pair
            stack.pop()
        slow = slow.next
        while slow is not None:
            if slow.val != stack.pop():
                return False
            slow = slow.next
        return True

vectors = [
        [1], True,
        [1,2,2,1], True,
        [1,2,3,4,5,6,6,5,4,3,2,1], True,
        [1,2], False,
        [1,1], True,
        [1,2,3,4,5,6,5,4,3,2,1], True
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    print(f'{a}')
    head = listnodes(a)
    expected = vectors[i + 1]
    returned = Solution().isPalindrome(head)
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}!'
