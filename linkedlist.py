class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListNodeIterator(object):
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is not None:
            val = self.current
            self.current = self.current.next
            return val
        else:
            raise StopIteration

def nodeslen(head):
    """
    Returns the length of the linked list.

    :type ListNode
    :rtype int
    """
    if head is None:
        return 0
    i = 0
    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        i += 1
    return 2 * i + (2 if fast is not None else 1)

def reversenodes(head):
    """
    Reverses a linked list and returns its head.

    :type ListNode
    :rtype ListNode
    """
    if head is None or head.next is None:
        return head
    prev, node = head, head.next
    head.next = None
    while node.next is not None:
        next_node = node.next
        node.next = prev
        prev, node = node, next_node
    node.next = prev
    return node

# Runtime complexity O(n^2)
def sortnodes(head, reverse=False):
    """
    Sorts the list and returns its new head.

    :type ListNode
    :rtype ListNode
    """
    if head is None or head.next is None:
        return head
    # ascending order
    compare = lambda e1, e2: e1.val > e2.val
    if reverse:
        # descending order
        compare = lambda e1, e2: e1.val < e2.val
    # insertion sort
    head = ListNode(0, head)
    prev = head.next
    node = head.next.next
    while node is not None:
        if compare(node, prev):
            prev = prev.next
            node = node.next
            continue
        temp = head
        while compare(node, temp.next):
            temp = temp.next
        prev.next = node.next
        node.next = temp.next
        temp.next = node
        node = prev.next
    return head.next

def listnodes(iterable):
    if iterable is None:
        return None
    assert len(iterable) > 0, f'TODO: think about this case'
    head = ListNode(iterable[0])
    node = head
    for value in iterable[1:]:
        node.next = ListNode(value)
        node = node.next
    assert node.next == None
    return head

def nodestolist(listnode):
    if listnode is None:
        return None
    _list = []
    for node in ListNodeIterator(listnode):
        _list.append(node.val)
    return _list

def printnodes(head):
    s = ', '.join(str(node.val) for node in ListNodeIterator(head))
    print('Nodes[' + s +']')

# it's called Node in https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/
class TriNode(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def trinodes(iterable):
    assert iterable != None or len(iterable) > 0
    head = TriNode(iterable[0], None, None, None)
    if len(iterable) == 1:
        return head
    node = head
    for value in iterable[1:]:
        node.next = TriNode(value, node, None, None)
        node = node.next
    assert node.next == None
    return head
