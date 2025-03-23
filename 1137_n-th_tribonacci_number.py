class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib = [0, 1, 1, 0]
        if n < 3:
            return fib[n]
        for i in range(3, n + 1):
            fib[-1] = fib[2] + fib[1] + fib[0]
            fib[0] = fib[1]
            fib[1] = fib[2]
            fib[2] = fib[-1]
        return fib[-1]

vectors = [
        0, 0,
        1, 1,
        2, 1,
        3, 2,
        4, 4,
        5, 7,
        6, 13,
        7, 24,
        8, 44
        ]

for i in range(0, len(vectors), 2):
    n = vectors[i]
    expected = vectors[i + 1]
    print(f'{n} {expected}')
    returned = Solution().tribonacci(n)
    assert expected == returned, f'for {n} expected {expected}, returned {returned}'
