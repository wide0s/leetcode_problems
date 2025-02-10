# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from linkedlist import listnodes, ListNode, nodestolist

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # my slow solution
        #
        #if head is not None:
        #    head = ListNode(-1, head)
        #    n, node = 1, head.next
        #    while node.next is not None:
        #        node = node.next
        #        n += 1
        #    prev = head
        #    node = head.next
        #    for _ in range(n // 2):
        #        prev = node
        #        node = node.next
        #    prev.next = node.next
        #    node.next = None
        #    head = head.next
        #return head

        # If the linked list only has one node or zero node
        if head is None or head.next is None:
            return None

        slow, fast = head, head
        # Use to store the previous node of the slow pointer
        # Easier to remove the node
        prev = None
        
        # When the fast pointer doesn't point to None
        while fast and fast.next:
            #if prev is None:
            #    print(f' prev=None slow.val={slow.val} fast.val={fast.val}')
            #else:
            #    print(f' prev.val={prev.val} slow.val={slow.val} fast.val={fast.val}')
            prev = slow
            slow = slow.next
            fast = fast.next.next # it runs at speed x2 times faster
                                  # that the slow pointer

        prev.next = slow.next

        return head


vectors = [
        [1,2,3,4,5,6,7,8], [1,2,3,4,6,7,8],
        [1,3,4,7,1,2,6], [1,3,4,1,2,6],
        [1,2,3,4], [1,2,4],
        [2,1], [2],
        [1], None
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    print(f'{a}')
    expected = vectors[i+1]
    head = listnodes(a)
    returned = Solution().deleteMiddle(head)
    if type(returned) == type(head):
        returned = nodestolist(returned)
    assert expected == returned, f'for {a} expected {expected}, but returned {returned}'
