class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        fib_2 = 0
        fib_1 = 1
        fib = 0
        for i in range(2, n + 1):
            fib = fib_1 + fib_2
            fib_2 = fib_1
            fib_1 = fib
        return fib

vectors = [
        2, 1,
        3, 2,
        4, 3,
        5, 5,
        6, 8,
        7, 13,
        8, 21
        ]

for i in range(0, len(vectors), 2):
    n = vectors[i]
    expected = vectors[i + 1]
    returned = Solution().fib(n)
    assert expected == returned, f'for {n} expected {expected}, returned {returned}'
