# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def genll(_list):
    root = ListNode(_list[0])
    node = root
    for e in _list[1:]:
        node.next = ListNode(e)
        node = node.next
    return root

def printll(ll):
    while ll is not None:
        print(ll.val, end='')
        ll = ll.next
    print('')

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
        #print(v1)
        #print(v2)
        #print(v1 + v2)
        return root.next


printll(Solution().addTwoNumbers(genll([0]), genll([0])))
printll(Solution().addTwoNumbers(genll([2, 4, 3]), genll([5, 6, 4])))
