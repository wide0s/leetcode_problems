# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from linkedlist import listnodes, nodestolist

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = node
        while node.next is not None:
            prev = node
            node.val = node.next.val
            node = node.next
        prev.val = node.val
        prev.next = node = None

vectors = [
        [1,2,3], 2, [1,3],
        [1,2,3,4,5], 2, [1,3,4,5],
        [1,2,3,4,5], 3, [1,2,4,5],
        [1,2,3,4,5], 4, [1,2,3,5]
        ]

for i in range(0, len(vectors), 3):
    a = vectors[i]
    v = vectors[i+1]
    print(f'{a}, v={v}')
    expected = vectors[i+2]
    head = listnodes(a)
    node = tail = head
    while node.next is not None:
        if node.val == v:
            break
        node = node.next
    assert node != head, f'bad test: node must not point to the head!'
    assert node.next is not None, f'bad test: node must not point to the tail!'
    Solution().deleteNode(node)
    returned = nodestolist(head)
    assert expected == returned, f'for {a} and node {v} expected {expected}, but returned {returned}!'
