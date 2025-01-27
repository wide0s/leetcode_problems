class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        n, m = len(mat), len(mat[0])
        _list = [0] * (n * m)
        index = i = j = 0
        up = 1
        while index < n * m:
            _list[index] = mat[i][j]
            index += 1
            if up == 1:
                if i - 1 < 0:
                    up = 0
                    if j + 1 < m:
                        j += 1
                    else:
                        i += 1
                else:
                    if j + 1 < m:
                        i -= 1
                        j += 1
                    else:
                        up = 0
                        i += 1
            else:
                if i + 1 < n:
                    if j - 1 >= 0:
                        i += 1
                        j -= 1
                    else:
                        up = 1
                        i += 1
                else:
                    if j + 1 < m:
                        up = 1
                        j += 1
                    else:
                        # reached the bottom right
                        pass
        return _list


vectors = [
        [[1]], [1],
        [[2, 3]], [2, 3],
        [[1,2,3], [4,5,6], [7,8,9]], [1,2,4,7,5,3,6,8,9],
        [[1,2],[3,4]], [1,2,3,4],
]

for i in range(0, len(vectors), 2):
    matrix = vectors[i]
    expected = vectors[i + 1]
    print(matrix)
    returned = Solution().findDiagonalOrder(matrix)
    assert expected == returned, f'for {matrix} expected {expected}, returned {returned}'
