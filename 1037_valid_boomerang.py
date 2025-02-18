class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """

        def is_straight_line(points):
            if len(points) < 3:
                return True
            line = None
            v, n = 0, len(points)
            for i in range(1, n):
                dx = points[0][0] - points[i][0]
                dy = points[0][1] - points[i][1]
                k, b = float('inf'), points[0][0] # if dx = 0 => x = Const
                if dx != 0:
                    k = dy / float(dx)
                    b = (points[0][0] * points[i][1] - points[0][1] * points[i][0]) / float(dx)
                if line is None:
                    line = (k, b)
                elif (k, b) != line:
                    return False
            return True

        return points[0] != points[1] and \
                points[0] != points[2] and \
                points[1] != points[2] and \
                not is_straight_line(points)

vectors = [
        [[1,1],[2,3],[3,2]], True,
        [[1,1],[2,2],[3,3]], False,
        [[1,1],[2,2],[1,1]], False,
        [[0,0],[0,2],[2,1]], True
        ]

for i in range(0, len(vectors), 2):
    points = vectors[i]
    print(points)
    expected = vectors[i + 1]
    returned = Solution().isBoomerang(points)
    assert expected == returned, f'for {points} expected {expected}, but returned {returned}!'
