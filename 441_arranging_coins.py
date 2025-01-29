# You have n coins and you want to build a staircase with these coins.
# The staircase consists of k rows where the ith row has exactly i coins.
# The last row of the staircase may be incomplete.
#
# Given the integer n, return the number of complete rows of the staircase you will build.

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        row = 1
        while n >= row:
            n = n - row
            row += 1
        if n < row:
            row -= 1
        return row

vectors = [
        5, 2,
        8, 3
]

for i in range(0, len(vectors), 2):
    coins = vectors[i]
    expected = vectors[i + 1]
    returned = Solution().arrangeCoins(coins)
    assert expected == returned, f'for {coins} expected {expected}, returned {returned}'
