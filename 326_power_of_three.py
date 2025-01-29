# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3^x.

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        # 1162261467 (3^19) is max power of 3 for 32bits
        return n > 0 and 1162261467 % n == 0

vectors = [
        0, False,
        1, True,
        2, False,
        3, True,
        4, False,
        5, False,
        6, False,
        7, False,
        8, False,
        9, True,
        10, False,
        12, False,
        16, False,
        26, False,
        27, True,
        32, False,
        34, False,
        128, False,
        256, False
]

for i in range(0, len(vectors), 2):
    n = vectors[i]
    expected = vectors[i + 1]
    print(f'n={n}')
    returned = Solution().isPowerOfThree(n)
    assert expected == returned, f'for {n} expected {expected}, returned {returned}'
