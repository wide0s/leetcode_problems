# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4^x.

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        return n > 3 and n & (n - 1) == 0 and not (n & 0xAAAAAAAA)

vectors = [
        0, False,
        1, True,
        2, False,
        3, False,
        4, True,
        5, False,
        8, False,
        10, False,
        12, False,
        16, True,
        32, False,
        34, False,
        128, False,
        256, True
]

for i in range(0, len(vectors), 2):
    n = vectors[i]
    expected = vectors[i + 1]
    print(f'n={n}')
    returned = Solution().isPowerOfFour(n)
    assert expected == returned, f'for {n} expected {expected}, returned {returned}'
