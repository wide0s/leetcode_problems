#Given a positive integer n, return the smallest positive
#integer that is a multiple of both 2 and n.

class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n if n % 2 == 0 else 2*n

vectors = [
        5, 10,
        6, 6
        ]

for i in range(0, len(vectors), 2):
    n = vectors[i]
    expected = vectors[i+1]
    returned = Solution().smallestEvenMultiple(n)
    assert expected == returned, f'for {n} expected {expected}, but returned {returned}!'
