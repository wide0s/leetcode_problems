from linkedlist import listnodes, nodestolist

# THIS IS NOT MY SOLUTION: https://leetcode.com/problems/linked-list-cycle-ii/solutions/1701128/c-java-python-slow-and-fast-image-explanation-beginner-friendly/
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        else:
            # nice construct to leave while !
            return None
        while head != slow:
            head = head.next
            slow = slow.next
        return head
