from linkedlist import ListNode, listnodes, nodestolist, printnodes, reversenodes, sortnodes, nodeslen


# listnodes
vectors = [
        None,
        [1],
        [1,2,3,4,5,6]
        ]
for a in vectors:
    print(f'listnodes | {a}')
    head = listnodes(a)
    if a is None:
        assert head == None, f'listnodes | for {a} expected None, but returned {head}!'
    else:
        assert type(head) == ListNode, f'lsitnodes | type(head) must be TListNode, but it is {type(head)}!'
        i = 0
        while head is not None:
            assert head.val == a[i], f'listnodes | for node at index {i} expected {a[i]}, but returned {head.val}!'
            head = head.next
            i += 1

# nodeslen
vectors = [
        None, 0,
        [1], 1,
        [1,2,3,4,5,6], 6
        ]
for i in range(0, len(vectors), 2):
    a = vectors[i]
    expected = vectors[i + 1]
    print(f'nodeslen | {a}')
    head = listnodes(a)
    nlen = nodeslen(head)
    assert expected == nlen, f'nodeslen | for {a} expected {expected}, but returned {returned}!'

# nodestolist
vectors = [
        None,
        [1],
        [1,2,3,4,5,6]
        ]
for a in vectors:
    print(f'nodestolist | {a}')
    returned = nodestolist(listnodes([x for x in a]) if a is not None else None)
    assert a == returned, f'for {a} expected {a}, but returned {returned}!'

# printnodes
printnodes(listnodes(None))
printnodes(listnodes([1]))
printnodes(listnodes([1,2,3,4,5,6,7,8,9]))

# reversnodes
vectors = [
        None, None,
        [1], [1],
        [1,2], [2,1],
        [1,2,3,4,5,6,7,8,9,10], [10,9,8,7,6,5,4,3,2,1]
        ]
for i in range(0, len(vectors), 2):
    a = vectors[i]
    print(f'reversenodes | {a}')
    head = listnodes(a)
    expected = vectors[i + 1]
    returned = reversenodes(head)
    returned = nodestolist(returned)
    assert expected == returned, f'reversenodes | for {a} expected {expected}, but returned {returned}'

# sortnodes
vectors = [
        None, None,
        [1], [1],
        [10,-1,0,1,5,4,3,12,-9], [-9,-1,0,1,3,4,5,10,12],
        [11,10,9,8,7,6,5,4,3,2,1], [1,2,3,4,5,6,7,8,9,10,11]
        ]
for i in range(0, len(vectors), 2):
    a = vectors[i]
    print(f'sortnodes, ascending order | {a}')
    head = listnodes(a)
    expected = vectors[i + 1]
    returned = nodestolist(sortnodes(head))
    assert expected == returned, f'sortnodes, ascending order | for {a} expected {expected}, but returned {returned}!'

vectors = [
        None, None,
        [1], [1],
        [10,-1,0,1,5,4,3,12,-9], [12,10,5,4,3,1,0,-1,-9],
        [1,2,3,4,5,6,7,8,9,10,11], [11,10,9,8,7,6,5,4,3,2,1]
        ]
for i in range(0, len(vectors), 2):
    a = vectors[i]
    print(f'sortnodes, descending order | {a}')
    head = listnodes(a)
    expected = vectors[i + 1]
    returned = nodestolist(sortnodes(head, True))
    assert expected == returned, f'sortnodes, descending order | for {a} expected {expected}, but returned {returned}!'
