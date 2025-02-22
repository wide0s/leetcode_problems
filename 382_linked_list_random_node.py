# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#FROM https://github.com/doocs/leetcode/blob/main/solution/0300-0399/0382.Linked%20List%20Random%20Node/Solution.py
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head

    def getRandom(self):
        """
        :rtype: int
        """
        n = 1
        o = 0
        node = self.head
        while node is not None:
            r = random.randint(1, n)
            if n == r: # indeed we can test r against any number in [1,n], e.g. 1
                o = node.val
            node = node.next
            n += 1
        return o

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
