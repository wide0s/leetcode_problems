class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        area = 0
        for i in range(n):
            max_in_row = 0
            max_in_col = 0
            for j in range(n):
                if grid[i][j] != 0:
                    area += 1
                max_in_row = max(max_in_row, grid[i][j])
                max_in_col = max(max_in_col, grid[j][i])
            area += max_in_row + max_in_col
        return area

vectors = [
        [[1,2], [3,4]], 17,
        [[2]], 5,
        [[1,0], [0,2]], 8
]

for i in range(0, len(vectors), 2):
    matrix = vectors[i]
    expected = vectors[i + 1]
    print(matrix)
    returned = Solution().projectionArea(matrix)
    assert expected == returned, f"for {matrix} expected {expected}, returned {returned}!"
