from linkedlist import listnodes, nodestolist, sortnodes2

vectors = [
        None, None,
        [1], [1],
        [10,-1,0,1,5,4,3,12,-9], [-9,-1,0,1,3,4,5,10,12],
        [11,10,9,8,7,6,5,4,3,2,1], [1,2,3,4,5,6,7,8,9,10,11]
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    head = listnodes(a)
    expected = vectors[i + 1]
    returned = nodestolist(sortnodes2(head))
    assert expected == returned, f'sort in ascending order: for {a} expected {expected}, but returned {returned}!'

vectors = [
        None, None,
        [1], [1],
        [10,-1,0,1,5,4,3,12,-9], [12,10,5,4,3,1,0,-1,-9],
        [1,2,3,4,5,6,7,8,9,10,11], [11,10,9,8,7,6,5,4,3,2,1]
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    head = listnodes(a)
    expected = vectors[i + 1]
    returned = nodestolist(sortnodes2(head, True))
    assert expected == returned, f'sort in descending order: for {a} expected {expected}, but returned {returned}!'
