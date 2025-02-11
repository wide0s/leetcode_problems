from linkedlist import listnodes, nodestolist

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is not None:
            slow, fast = head, head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if slow == fast:
                    return True
        return False

returned = Solution().hasCycle(None)
assert returned == False, f'for None expected False, but returned {returned}!'

a = [3,2,0,-4]
head = listnodes(a)
head.next.next.next = head.next
expected = True
assert Solution().hasCycle(head) == expected, f'for {a} expected {expected}, but returned {returned}!'

a = [1,2]
head = listnodes(a)
head.next = head
expected = True
assert Solution().hasCycle(head) == expected, f'for {a} expected {expected}, but returned {returned}!'

a = [1]
head = listnodes(a)
expected = False
assert Solution().hasCycle(head) == expected, f'for {a} expected {expected}, but returned {returned}!'
