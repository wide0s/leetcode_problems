# You are given an n x n 2D matrix representing an image,
# rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you
# have to modify the input 2D matrix directly. DO NOT allocate
# another 2D matrix and do the rotation.

class Solution(object):
    def generateMatrix(self, n):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def spiral(n):
            rows = columns = n
            x = y = 0 # initial cell
            while rows > 0 and columns > 0:
                i = j = 0
                # moving to the right
                if columns < 1:
                    break
                for j in range(columns):
                    yield (x, y + j)
                rows -= 1
                # moving down
                if rows < 1:
                    break
                for i in range(1, rows + 1):
                    yield (x + i, y + j)
                columns -= 1
                # moving to the left
                if columns < 1:
                    break
                for j in range(1, columns + 1):
                    yield (x + i, y + columns - j)
                j = columns - j
                rows -= 1
                # moving up
                if rows < 1:
                    break
                for i in range(0, rows):
                    yield (x + rows - i, y + j)
                i = rows - i
                columns -= 1
                # setting the initial cell [x][y]
                x += i
                y += j + 1

        mat = [ [0] * n for _ in range(n) ]
        V = 0
        for i, j in spiral(n):
            mat[i][j] = V = V + 1

        return mat

vectors = [
        [[1]],
        [[1, 2], [4, 3]],
        [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
]

for i in range(len(vectors)):
    result = Solution().generateMatrix(i + 1)
    assert result == vectors[i], f'for n should be {vectors[i]}, obtained {result}'
