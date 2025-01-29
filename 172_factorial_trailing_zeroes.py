# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
#
# https://www.purplemath.com/modules/factzero.htm

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        assert n >= 0
        if n < 5:
            return 0
        zeroes, divisor = 0, 5
        while divisor <= n:
            zeroes += n // divisor
            divisor *= 5
        return zeroes

vectors = [
        0, 0,
        1, 0,
        2, 0,
        3, 0,
        4, 0,
        5, 1,
        23, 4,
        101, 24,
        4617, 1151
]

for i in range(0, len(vectors), 2):
    n = vectors[i]
    expected = vectors[i + 1]
    print(f'counting traling zeroes for {n}!')
    returned = Solution().trailingZeroes(n)
    assert expected == returned, f'for {n} expected {expected}, returned {returned}'
