from linkedlist import ListNode, listnodes, printnodes, nodestolist

# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's 
# nodes (i.e., only nodes themselves may be changed.)

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        node = prev = head
        update_head = True
        while node is not None and node.next is not None:
            next_node = node.next
            node.next = node.next.next
            next_node.next = node
            if update_head:
                head = next_node
                update_head = False
            else:
                prev.next = next_node
                prev = node
            node = node.next
        return head

vectors = [ [ 1, 2, 3, 4, 5, 6 ], [ 2, 1, 4, 3, 6, 5 ], [ 1 ], [ 1 ], [ 1, 2, 3, 3, 5 ], [ 2, 1, 3, 3, 5 ] ]
for i in range(0, len(vectors), 2):
    swaped = Solution().swapPairs(listnodes(vectors[i]))
    printnodes(swaped)
    assert nodestolist(swaped) == vectors[i + 1]
