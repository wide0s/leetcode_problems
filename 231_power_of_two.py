# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2^x.


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (~n + 1)) == n

vectors = [
        0, False,
        1, True,
        2, True,
        3, False,
        4, True,
        5, False,
        8, True,
        10, False,
        12, False,
        16, True,
        32, True,
        34, False,
        128, True,
        130, False
]

for i in range(0, len(vectors), 2):
    n = vectors[i]
    expected = vectors[i + 1]
    print(f'n={n}')
    returned = Solution().isPowerOfTwo(n)
    assert expected == returned, f'for {n} expected {expected}, returned {returned}'
