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

def listnodes(iterable):
    assert iterable != None or len(iterable) > 0
    head = ListNode(iterable[0])
    node = head
    for value in iterable[1:]:
        node.next = ListNode(value)
        node = node.next
    assert node.next == None
    return head

def nodestolist(listnode):
    _list = []
    for node in ListNodeIterator(listnode):
        _list.append(node.val)
    return _list

def printnodes(head):
    node = head
    print('<', end='')
    while node is not None:
        print(node.val, end='>' if node.next == None else ', ')
        node = node.next
    print('')
