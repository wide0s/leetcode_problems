# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

# Input = [
#     [1,2,3,4],
#     [5,1,2,3],
#     [9,5,1,2]
# ]
#      
# Output: True

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n, m = len(matrix), len(matrix[0])

        for i in range(n - 1):
            for j in range(m - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True

vectors = [
        [[1]], True,
        [[1, 2]], True,
        [[1], [2]], True,
        [[1,2,3,4], [5,1,2,3], [9,5,1,2]], True,
        [[1,2], [2,2]], False,
        [[1,1], [2, 2]], False
]

for i in range(0, len(vectors), 2):
    matrix = vectors[i]
    expected = vectors[i + 1]
    print(f'{matrix} {expected}')
    result = Solution().isToeplitzMatrix(matrix)
    assert result == expected, f"for {matrix} expected {expected}, returned {result}!"
