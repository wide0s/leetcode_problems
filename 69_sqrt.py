# Given a non-negative integer x, return the square root of x
# rounded down to the nearest integer. The returned integer
# should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
#
# Constraints:
#  0 <= x <= 2^31 - 1

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        def perfect_square(x):
            lo, hi = 0, x
            while lo < hi:
                mid = (hi + lo) // 2
                if mid * mid < x:
                    lo = mid + 1
                else:
                    hi = mid
            if lo * lo > x:
                lo = lo - 1
            return lo
        return perfect_square(x)

vectors = [
        0, 0,
        1, 1,
        4, 2,
        8, 2,
        9, 3,
        17, 4
        ]

for i in range(0, len(vectors), 2):
    x = vectors[i]
    print(x)
    expected = vectors[i+1]
    returned = Solution().mySqrt(x)
    assert expected == returned, f'for {x} expected {expected}, but returned {returned}!'
