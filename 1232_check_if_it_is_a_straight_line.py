class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) < 3:
            return True
        line = None
        v, n = 0, len(coordinates)
        for i in range(1, n):
            dx = coordinates[0][0] - coordinates[i][0]
            dy = coordinates[0][1] - coordinates[i][1]
            k, b = float('inf'), coordinates[0][0] # if dx = 0 => x = Const
            if dx != 0:
                k = dy / float(dx)
                b = (coordinates[0][0] * coordinates[i][1] - coordinates[0][1] * coordinates[i][0]) / float(dx)
            if line is None:
                line = (k, b)
            elif (k, b) != line:
                return False
        return True

vectors = [
        [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]], False,
        [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]], True
        ]
for i in range(0, len(vectors), 2):
    coordinates = vectors[i]
    print(coordinates)
    expected = vectors[i+1]
    returned = Solution().checkStraightLine(coordinates)
    assert returned == expected, f'for {coordinates} expected {expected}, but returned {returned}!'
