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
        # Let n be a strictly palindromic number for any
        # natural base b \in [2,n−2], then writing it for
        # the base n−2, we obtain the expression 
        # 1∗(n−2)^1 + 2∗(n−2)^0 or 12 (base n-2), which
        # is clearly not a palindromic number for any
        # base n−2.
        return False

vectors = [
        9, False,
        4, False
        ]

for i in range(0, len(vectors), 2):
    n = vectors[i]
    expected = vectors[i+1]
    print(f'{n} {expected}')
    returned = Solution().isStrictlyPalindromic(n)
    assert expected == returned, f'for {n} expected {expected}, but returned {returned}!'
