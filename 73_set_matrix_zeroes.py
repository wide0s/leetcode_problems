# Given an m x n integer matrix matrix, if an element is 0,
# set its entire row and column to 0's.
# You must do it in place.
#
# Input = [        Output = [
#     [1,1,1],         [1,0,1],
#     [1,0,1],         [0,0,0],
#     [1,1,1]          [1,0,1]
# ]
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])

        def zeroing(matrix, i, j, visited={}, skip_visited = True, \
                directions=['U', 'D', 'L', 'R']):
            if i < 0 or j < 0 or i >= n or j >= m or \
                    (skip_visited and (i, j) in visited):
                return
            #                  U
            #              [i - 1, j]
            # L [i, j - 1 ][i,     j][i, j + 1] R
            #              [i + 1, j]
            #                  D
            if matrix[i][j] != 0:
                visited[(i, j)] = matrix[i][j]
                matrix[i][j] = 0

            for direction in directions:
                if direction == 'U':
                    zeroing(matrix, i - 1, j, visited, False, [direction])
                elif direction == 'D':
                    zeroing(matrix, i + 1, j, visited, False, [direction])
                elif direction == 'L':
                    zeroing(matrix, i, j - 1, visited, False, [direction])
                elif direction == 'R':
                    zeroing(matrix, i, j + 1, visited, False, [direction])

        visited = {}
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zeroing(matrix, i, j, visited)
        #print(visited)

vectors = [
        [[1,1,1], [1,0,1], [1,1,1]], [[1,0,1], [0,0,0], [1,0,1]],
        [[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]],
        [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]], [[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
]

for i in range(0, len(vectors), 2):
    #print(vectors[i])
    Solution().setZeroes(vectors[i])
    assert vectors[i] == vectors[i + 1], f"for {i} should be {vectors[i + 1]}, returned {vectors[i]}"
