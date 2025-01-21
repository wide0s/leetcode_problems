class Solution2(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        fib = [1, 2]
        for i in range(2, n):
            reg = fib[-1]
            fib[-1] += fib[-2]
            fib[-2] = reg
        return fib[-1]


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def calc(n, w = 0):
            if n > 1:
                return calc(n - 1, w) + calc(n - 2, w)
            return w + 1
        return calc(n)

for i in range(45):
    print(f'{i + 1} {Solution2().climbStairs(i + 1)}')
