# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import ListNode, listnodes, nodestolist

class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or nums is None \
                or len(nums) == 0:
            return head
        nset = set(nums)
        head = ListNode(0xdeadbeaf, head)
        prev = head
        node = head.next
        while node is not None:
            if node.val in nset:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return head.next

vectors = [
        None, [1], None,
        [1,2,3,4,5], [1,2,3], [4,5],
        [1,2,1,2,1,2], [1], [2,2,2],
        [1,2,3,4], [5], [1,2,3,4],
        [1,2,3], [1,3], [2],
        [1,2,3], [1,2,3], None
        ]

for i in range(0, len(vectors), 3):
    a = vectors[i]
    nums = vectors[i + 1]
    print(f'{a}, {nums}')
    head = listnodes([ x for x in a ] if a is not None else None)
    expected = vectors[i + 2]
    returned = Solution().modifiedList(nums, head)
    returned = nodestolist(returned)
    assert expected == returned, f'for {a} and {nums} expected {expected}, but returned {returned}!'
