class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        divisors = 2
        for i in range(2, n - 1):
            if n % i == 0:
                divisors += 1
            if divisors > 3:
                break
        return divisors == 3

vectors = [
        1, False,
        2, False,
        3, False,
        4, True,
        5, False,
        6, False,
        7, False,
        8, False,
        9, True
        ]

for i in range(0, len(vectors), 2):
    n = vectors[i]
    expected = vectors[i+1]
    returned = Solution().isThree(n)
    assert expected == returned, f'for {n} expected {expected}, but returned {returned}!'
