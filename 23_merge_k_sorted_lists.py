from linkedlist import ListNode, listnodes, printnodes, nodestolist
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        merge = None
        for llist in lists:
            node = llist
            while node is not None:
                if not merge:
                    merge = []
                merge.append(node.val)
                node = node.next
        if not merge:
            return None
        node = head = None
        for value in sorted(merge):
            if not head:
                head = ListNode(value)
                node = head
            else:
                node.next = ListNode(value)
                node = node.next
        return head

merge = Solution().mergeKLists([listnodes([1,4,5]), listnodes([1,3,4]), listnodes([2,6])])
printnodes(merge)
assert nodestolist(merge) == [1,1,2,3,4,4,5,6]
