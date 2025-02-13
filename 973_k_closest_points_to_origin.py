from math import sqrt

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        return sorted(points, key=lambda p: sqrt(p[0]*p[0] + p[1]*p[1]))[:k]

vectors = [
        [[1,3],[-2,2]], 1, [[-2,2]],
        [[3,3],[5,-1],[-2,4]], 2, [[3,3],[-2,4]]
        ]
for i in range(0, len(vectors), 3):
    points = vectors[i]
    k = vectors[i+1]
    print(f'{points}, k={k}')
    expected = vectors[i+2]
    returned = Solution().kClosest(points, k)
    assert returned == expected, f'for {points} expected {expected}, but returned {returned}!'
