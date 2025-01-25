# You are given an m x n integer matrix matrix with the following two properties:
#
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.

class Solution(object):
    def searchMatrix(self, mat, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n, m = len(mat), len(mat[0])
        assert n * m != 0
        if n * m == 1 and target == mat[0][0]:
            return True
        left, right = 0, n * m
        while left < right:
            mid = (right + left) // 2
            # core trick for matching index in an 1D array
            # to a cell in a 2D matrix
            if n == 1:
                i = 0
                j = mid
            else:
                i = mid // m
                j = mid % m
            if mat[i][j] < target:
                left = mid + 1
            elif mat[i][j] > target:
                right = mid
            else:
                return True
        return False

vectors = [
    [[1]], 0, 2,
    [[1], [4]], 0, 3,
    [[1], [4], [100]], 0, 3,
    [[1], [4], [40], [4]], 0, 24,
    [[1,20]], 0, 18,
    [[1,2,30]], 3, 29,
    [[1,28,30,56]], 27, 54,
    [[1,3,5,7], [10,11,16,20], [23,30,34,60]], 0, 59
]

for i in range(0, len(vectors), 3):
    matrix = vectors[i]
    print(matrix)
    n, m = len(matrix), len(matrix[0])
    for x in range(n):
        for y in range(m):
            target = matrix[x][y]
            assert Solution().searchMatrix(matrix, target) == True, f'{matrix}, target={target}: expected True, returned False!'
    for j in range(1, 3):
        target = vectors[i + j]
        assert Solution().searchMatrix(matrix, target) == False, f'{matrix}, target={target}: expected False, returned True!'
