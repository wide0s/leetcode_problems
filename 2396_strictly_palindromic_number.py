# An integer n is strictly palindromic if, for every base 
# b between 2 and n - 2 (inclusive), the string representation
# of the integer n in base b is palindromic.
#
# Given an integer n, return true if n is strictly palindromic
# and false otherwise.
#
# A string is palindromic if it reads the same forward and backward.

class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False

vectors = [
        9, False,
        4, False
        ]

for i in range(0, len(vectors), 2):
    n = vectors[i]
    expected = vectors[i+1]
    returned = Solution().isStrictlyPalindromic(n)
    assert expected == returned, f'for {n} expected {expected}, but returned {returned}!'
