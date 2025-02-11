class MyNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.n = 0

    def __repr__(self):
        if self.head is None:
            return f'LL[{self.n}][]'
        o, node = [], self.head
        while node.next != self.head:
            o.append(node.val)
            node = node.next
        o.append(node.val)
        return f'LL[{self.n}][' + ', '.join(str(x) for x in o) + ']'

    def _find_node(self, index, safe=True):
        """
        :type index: int
        :type safe: bool
        :rtype: MyList
        """
        upper_limit = self.n if safe else self.n + 1
        if self.head is not None and 0 <= index < upper_limit:
            node = self.head
            if index <= self.n // 2:
                for i in range(0, index):
                    node = node.next
            else:
                for i in range(0, self.n - index):
                    node = node.prev
            return node
        return None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        node = self._find_node(index, True)
        return node.val if node is not None else -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head is None:
            self.head = MyNode(val)
            self.head.next = self.head
            self.head.prev = self.head
        else:
            node = MyNode(val, self.head, self.head.prev)
            self.head.prev.next = node
            self.head.prev = node
            self.head = node
        self.n += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head is None:
            self.head = MyNode(val)
            self.head.next = self.head
            self.head.prev = self.head
        else:
            node = MyNode(val, self.head, self.head.prev)
            self.head.prev.next = node
            self.head.prev = node
        self.n += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if 0 <= index <= self.n: # index can be == n!
            if self.head is None or index == 0:
                self.addAtHead(val)
            else:
                node = self._find_node(index, False)
                new_node = MyNode(val, node, node.prev)
                node.prev.next = new_node
                node.prev = new_node
                self.n += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if self.head is not None and 0 <= index < self.n:
            node = self._find_node(index, True)
            if self.n > 1:
                node.prev.next = node.next
                node.next.prev = node.prev
                if node == self.head:
                    self.head = node.next
                node.next = node.prev = None
            else:
                # this is the last node
                self.head.prev = self.head.next \
                        = self.head = None
            self.n -= 1

print('#1: empty list')
mylist = MyLinkedList()
print(f'MyLinkedList(): {mylist}')
assert mylist.get(-1) == -1
assert mylist.get(0) == -1
assert mylist.get(1) == -1
mylist.addAtIndex(-1, -1)
print(f'addAtindex(-1, -1) {mylist}')
assert mylist.n == 0
assert mylist.head == None
mylist.addAtIndex(1, 1)
print(f'addAtindex(1, 1) {mylist}')
assert mylist.n == 0
assert mylist.head == None
mylist.deleteAtIndex(0)
print(f'deleteAtIndex(0) {mylist}')
assert mylist.n == 0
assert mylist.head == None

print('#2: add 2 heads, delete, add tail, delete...')
mylist.addAtHead(0)
print(f'addAtHead(0): {mylist}')
assert mylist.n == 1
assert mylist.head.val == 0
assert mylist.get(0) == 0
mylist.addAtHead(-10)
print(f'addAtHead(-10): {mylist}')
assert mylist.n == 2
assert mylist.head.val == -10
assert mylist.get(0) == -10
assert mylist.get(1) == 0
mylist.deleteAtIndex(0)
print(f'deleteAtIndex(0) {mylist}')
assert mylist.n == 1
assert mylist.head.val == 0
assert mylist.get(0) == 0
assert mylist.get(1) == -1
mylist.addAtTail(10)
print(f'addAtTail(10) {mylist}')
assert mylist.n == 2
assert mylist.head.val == 0
assert mylist.get(0) == 0
assert mylist.get(1) == 10
mylist.deleteAtIndex(2)
print(f'deleteAtIndex(2) {mylist}')
assert mylist.n == 2
assert mylist.head.val == 0
assert mylist.get(0) == 0
assert mylist.get(1) == 10
mylist.deleteAtIndex(-1)
print(f'deleteAtIndex(-1) {mylist}')
assert mylist.n == 2
assert mylist.head.val == 0
assert mylist.get(0) == 0
assert mylist.get(1) == 10
mylist.deleteAtIndex(0)
print(f'deleteAtIndex(0) {mylist}')
assert mylist.n == 1
assert mylist.head.val == 10
assert mylist.get(0) == 10
assert mylist.get(1) == -1
mylist.deleteAtIndex(1)
print(f'deleteAtIndex(1) {mylist}')
assert mylist.n == 1
assert mylist.head.val == 10
assert mylist.get(0) == 10
assert mylist.get(1) == -1
mylist.deleteAtIndex(0)
print(f'deleteAtIndex(0) {mylist}')
assert mylist.n == 0
assert mylist.head == None
assert mylist.get(0) == -1
assert mylist.get(1) == -1

print('#3: add at index, delete...')
mylist.addAtIndex(0, 99)
print(f'addAtIndex(0, 99): {mylist}')
assert mylist.n == 1
assert mylist.head.val == 99
assert mylist.get(0) == 99
mylist.addAtIndex(0, 98)
print(f'addAtIndex(0, 98): {mylist}')
assert mylist.n == 2
assert mylist.head.val == 98
assert mylist.get(0) == 98
assert mylist.get(1) == 99
mylist.addAtIndex(2, 100)
print(f'addAtIndex(2, 100): {mylist}')
assert mylist.n == 3
assert mylist.head.val == 98
assert mylist.get(0) == 98
assert mylist.get(1) == 99
assert mylist.get(2) == 100
mylist.addAtIndex(4, 100)
print(f'addAtIndex(4, 100): {mylist}')
assert mylist.n == 3
assert mylist.head.val == 98
assert mylist.get(0) == 98
assert mylist.get(1) == 99
assert mylist.get(2) == 100
mylist.deleteAtIndex(1)
print(f'deleteAtIndex(1) {mylist}')
assert mylist.n == 2
assert mylist.head.val == 98
assert mylist.get(0) == 98
assert mylist.get(1) == 100
assert mylist.get(2) == -1
mylist.deleteAtIndex(1)
print(f'deleteAtIndex(1) {mylist}')
assert mylist.n == 1
assert mylist.head.val == 98
assert mylist.get(0) == 98
assert mylist.get(1) == -1
mylist.deleteAtIndex(0)
print(f'deleteAtIndex(0) {mylist}')
assert mylist.n == 0
assert mylist.head == None
assert mylist.get(0) == -1

print('#4: add, get, delete...')
num = 6
mylist.addAtIndex(0, 0)
for i in range(1, num):
    mylist.addAtHead(-i)
    mylist.addAtTail(i)
print(mylist)
assert mylist.get(num - 1) == 0
for i in range(0, num - 1):
    index = mylist.get(i)
    assert index == i + 1 - num, f'for index {i} expected {i + 1 - num}, returned {index}'
for i in range(num, 2*num - 1):
    index = mylist.get(i)
    assert index == i + 1 - num, f'for index {i} expected {i + 1 - num}, returned {index}'
assert mylist.get(2 * num) == -1
for i in range(0, 2 * num - 1):
    mylist.deleteAtIndex(0)
assert mylist.n == 0
assert mylist.head == None

print('#5: leetcode example')
mylist = MyLinkedList()
print(f'MyLinkedLost(): {mylist}')
mylist.addAtIndex(0, 1)
print(f'addAtIndex(0, 1): {mylist}')
mylist.addAtTail(3)
print(f'addAtTail(3): {mylist}')
mylist.addAtIndex(1, 2) # linked list becomes 1->2->3
print(f'addAtIndex(1, 2): {mylist}')
index = mylist.get(1) # return 2
assert index == 2
mylist.deleteAtIndex(1) # now the linked list is 1->3
print(f'deleteAtIndex(1): {mylist}')
index = mylist.get(1) # return 3
assert index == 3
