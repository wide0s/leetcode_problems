from linkedlist import listnodes, nodestolist, ListNode

class Solution(object):
    def convLLToInt(self, llist):
        v = 0
        k = 1
        while llist is not None:
            v += llist.val * k
            llist = llist.next
            k *= 10
        return v

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        v = self.convLLToInt(l1) + self.convLLToInt(l2)
        if v == 0:
            return ListNode(0)
        node = root = ListNode(0)
        while v > 0:
            r = v % 10
            v = v // 10
            node.next = ListNode(r)
            node = node.next 
        return root.next

vectors = [
    [0], [0], [0],
    [2, 4, 3], [5, 6, 4], [7, 0, 8]
]

for i in range(0, len(vectors), 3):
    l1 = vectors[i]
    l2 = vectors[i + 1]
    expected = vectors[i + 2]
    print(f'{l1} {l2} {expected}')
    returned = Solution().addTwoNumbers(listnodes(l1), listnodes(l2))
    assert expected == nodestolist(returned), f'for l1 = {l1} l2 = {l2} expected {expected}, returned {nodestolist(returned)}!'
