from linkedlist import trinodes, nodestolist

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None or (head.next is None and head.child is None):
            return head
        ladder = []
        node = head
        while (node.next is not None or node.child is not None):
            # --
            #childs = node.child is not None
            #prev = None if node.prev is None else node.prev.val
            #print(f'node={node.val} prev={prev} childs={childs}')
            # --
            if node.child is not None:
                ladder.append(node) # O(1) vs ladder += [node]
                node = node.child
            else:
                node = node.next
            if node.next is None and len(ladder) > 0:
                parent = ladder.pop() # O(1)
                node.next = parent.next
                if parent.next is not None:
                    parent.next.prev = node
                if parent.child.prev is None:
                    parent.next = parent.child
                    parent.child.prev = parent
                else:
                    assert parent.child.prev == None, "parent.child points to a non-head element!"
                # --
                #prev = None if node.prev is None else node.prev.val
                #nnext = None if node.next is None else node.next.val
                #print(f' node={node.val} prev={prev} next={nnext}')
                # --
                parent.child = None
        #childs = node.child is not None
        #print(f'{node.val} {node.prev.val} childs={childs}')
        return head

print('case 1')
returned = Solution().flatten(None)
assert returned is None, f'case #1: expected {expected}, but returned {returned}'

print('case 2')
layer3 = trinodes([331,332,333])
layer3.next.child = trinodes([3321])
layer2 = trinodes([31,32,33,34,35])
layer2.next.next.child = layer3
head = trinodes([1,2,3,4,5,6,7,8,9])
head.next.next.child = layer2
head.next.next.next.next.child = trinodes([51,52])
expected = [1,2,3,31,32,33,331,332,3321,333,34,35,4,5,51,52,6,7,8,9]
returned = nodestolist(Solution().flatten(head))
assert expected == returned, f'case #2.1: expected {expected}, but returned {returned}'
node = head
while node is not None:
    assert node.child is None, f'case #2.2: node {node.val} still has childs!'
    node = node.next
# check the integrity of the reversed list (prev pointer logic)
expected = [9,8,7,6,52,51,5,4,35,34,333,3321,332,331,33,32,31,3,2,1]
returned = []
tail = head
while tail.next is not None:
    tail = tail.next
expected_length = len(expected)
while tail is not None:
    assert expected_length > 0, f'case 2.3: expected {expected}, but returned {returned}'
    returned += [tail.val]
    tail = tail.prev
    expected_length -= 1
assert expected == returned and expected_length == 0, f'case #2.3: expected {expected}, but returned {returned}'

print('case 3')
head = trinodes([1,2,3])
head.child = trinodes([11,12])
expected = [1,11,12,2,3]
returned = nodestolist(Solution().flatten(head))
assert expected == returned, f'case #3: expected {expected}, but returned {returned}'

print('case 4')
head = trinodes([1])
head.child = trinodes([11,12])
expected = [1,11,12]
returned = nodestolist(Solution().flatten(head))
assert expected == returned, f'case #4: expected {expected}, but returned {returned}'

print('case 5')
head = trinodes([1])
expected = [1]
returned = nodestolist(Solution().flatten(head))
assert expected == returned, f'case #5: expected {expected}, but returned {returned}'

print('case 6')
layer2 = trinodes([11])
layer2.child = trinodes([111])
head = trinodes([1])
head.child = layer2
expected = [1,11,111]
returned = nodestolist(Solution().flatten(head))
assert expected == returned, f'case #6: expected {expected}, but returned {returned}'

print('case 7')
layer2 = trinodes([21,22])
layer2.next.child = trinodes([221])
head = trinodes([1,2])
head.next.child = layer2
expected = [1,2,21,22,221]
returned = nodestolist(Solution().flatten(head))
assert expected == returned, f'case #7: expected {expected}, but returned {returned}'
