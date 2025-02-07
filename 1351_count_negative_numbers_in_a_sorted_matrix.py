# Given a m x n matrix grid which is sorted in non-increasing
# order both row-wise and column-wise, return the number of
# negative numbers in grid.
#
# Constraints:
#  m == grid.length
#  n == grid[i].length
#  1 <= m, n <= 100
#  -100 <= grid[i][j] <= 100

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        def bisection(a):
            left, right = 0, len(a)
            while left < right:
                mid = (right + left) // 2
                if a[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid
            return left
        negatives = 0
        for i in range(n):
            j = bisection(grid[i])
            negatives += \
                    (m - j) if j < m else 0 
        return negatives

vectors = [
        [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]], 8,
        [[3,2],[1,0]], 0,
        [[3, -1],[-1,-2]], 3,
        [[1, 2]], 0,
        [[1, -1]], 1,
        [[1, -1, -2]], 2,
        [[1], [2]], 0,
        [[1], [-1]], 1,
        ]

for i in range(0, len(vectors), 2):
    grid = vectors[i]
    print(grid)
    expected = vectors[i+1]
    returned = Solution().countNegatives(grid)
    assert expected == returned, f'for {grid} expected {expected}, but returned {returned}!'
