from bisect import bisect

for i in range(20):
    a = [ x for x in range(i) ]
    for j, target in enumerate(a):
        assert bisect(a, target) == j
    assert bisect(a, -1) == -1
    assert bisect(a, len(a)) == -1

vectors = [
        [1, 2, 3, 4], 0, 3, 4, -1,
        [1, 2, 3, 4], 1, 4, 1, -1,
        [1, 2, 3, 4], 2, None, 3, 2,
        [1, 2, 3, 4], 1, 4, 3, 2
]

for i in range(0, len(vectors), 5):
    a = vectors[i]
    left = vectors[i + 1]
    right = vectors[i + 2]
    target = vectors[i + 3]
    expected = vectors[i + 4]
    assert bisect(a, target, left, right) == expected
