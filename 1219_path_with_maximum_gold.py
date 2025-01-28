class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return 0

            gold = grid[i][j]
            grid[i][j] = 0 # mark as visited for this search

            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            total_gold = gold + max(dfs(grid, i + di, j + dj) for di, dj in directions)

            grid[i][j] = gold # mark as unvisited for the next searches
            return total_gold

        return max(dfs(grid, i, j) for i in range(n) for j in range(m))

vectors = [
        [[0,6,0],[5,8,7],[0,9,0]], 24,
        [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]], 28,
        [[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,3,1,0,2,0],[3,0,5,0,20,0]], 60,
        [[0,0,0,22,0,24],[34,23,18,0,23,2],[11,39,20,12,0,0],[39,8,0,2,0,1],[19,32,26,20,20,30],[0,38,26,0,29,31]], 478
]

for i in range(0, len(vectors), 2):
    print(vectors[i])
    expected = vectors[i + 1]
    result = Solution().getMaximumGold(vectors[i])
    assert result == expected, f"for {vectors[i]} expected {expected}, returned {result}!"
