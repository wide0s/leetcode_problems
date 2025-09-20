class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        tab = [[6, 9], [7, 12], [8, 18]]
        memorized = [[2, 1], [3, 2], [4, 4], [5, 6]] + tab # products of 2, 3, ..., 8
        if n < 9:
            return memorized[n - 2][1]
        for i in range(9, n + 1, 3):
            for k in range(min(3, n - i + 1)):
                tab[k][1] = (i + k - tab[k][0]) * tab[k][1]
                tab[k][0] = i + k
        return tab[k][1]

vectors = [
    [2, 1],
    [3, 2],
    [6, 9],
    [10, 36]
]

for vector in vectors:
    params = vector[0]
    expected = vector[1]
    print(f'for n = {params} max product is {expected}')
    returned = Solution().integerBreak(params)
    assert expected == returned, f'for {params} expected {expected}, returned {returned}'