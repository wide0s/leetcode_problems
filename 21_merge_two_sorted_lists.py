from linkedlist import listnodes, printnodes, nodestolist

#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists into one sorted list. The list should be made
#by splicing together the nodes of the first two lists.
#Return the head of the merged linked list.

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list
        if not list2:
            return list1
        left, right = (list2, list1) if list2.val < list1.val else (list1, list2)

        merge = left
        while left is not None and right is not None:
            val = left.val if not left.next else left.next.val
            left_next = left.next
            while right is not None:
                if right.val > val:
                    if not left.next:
                        left.next = right
                        right = None
                    break
                left.next = right
                right = right.next
                left.next.next = left_next
                left = left.next
            left = left.next
        return merge

vectors = [ [ 1, 2, 4], [ 1, 3, 4], [ 1, 1, 2, 3, 4, 4 ], [ 1 ], [ 1 ], [ 1, 1 ], [ 4 ], [ 1, 2, 3 ], [ 1, 2, 3, 4] ]
for i in range(0, len(vectors), 3):
    merge = Solution().mergeTwoLists(listnodes(vectors[i]), listnodes(vectors[i + 1]))
    printnodes(merge)
    assert nodestolist(merge) == vectors[i + 2]
