from math import sqrt

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        vect = lambda p1, p2: [p2[0] - p1[0], p2[1] - p1[1]]
        ortho = lambda v1, v2: (v1[0] * v2[0] + v1[1] * v2[1]) == 0
        norm = lambda v: sqrt(v[0] * v[0] + v[1] * v[1])

        a = sorted([p1, p2, p3, p4], key = lambda x: (x[0], x[1]))

        v1 = vect(a[0],a[1])
        v2 = vect(a[1],a[3])
        v3 = vect(a[2],a[3])
        v4 = vect(a[0],a[2])

        n1 = norm(v1)
        n2 = norm(v2)
        n3 = norm(v3)
        n4 = norm(v4)

        return n1 * n2 * n3 * n4 != 0 and n1 == n2 == n3 == n4 \
                and ortho(v1,v2) and ortho(v2,v3) and ortho(v1,v4) and ortho(v4,v3)

vectors = [
        [0,0], [1,1], [1,0], [0,1], True,
        [0,0], [1,1], [1,0], [0,12], False,
        [1,0], [-1,0], [0,1], [0,-1], True,
        [0,0], [0,0], [0,0], [0,0], False
        ]

for i in range(0, len(vectors), 5):
    p1 = vectors[i]
    p2 = vectors[i + 1]
    p3 = vectors[i + 2]
    p4 = vectors[i + 3]
    expected = vectors[i + 4]
    print(f'{p1} {p2} {p3} {p4} {expected}')
    returned = Solution().validSquare(p1, p2, p3, p4)
    assert expected == returned, f'for {p1}, {p2}, {p3} and {p4} expected {expected}, but returned {returned}!'
