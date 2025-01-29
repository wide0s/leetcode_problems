# An ugly number is a positive integer which does not have
# a prime factor other than 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.

class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n // 5
            else:
                break
        return n == 1

vectors = [
        1, True,
        2, True,
        3, True,
        4, True,
        5, True,
        6, True,
        7, False,
        8, True,
        9, True,
        10, True,
        11, False,
        12, True,
        13, False,
        14, False,
        16, True,
        23, False,
        48, True,
        50, True,
        13500, True
]

for i in range(0, len(vectors), 2):
    number = vectors[i]
    expected = vectors[i + 1]
    print(f'number = {number}')
    returned = Solution().isUgly(number)
    assert expected == returned, f'for {number} expected {expected}, returned {returned}'
