class Solution(object):
    def isPerfectSquare(self, n):
        if n == 0:
            return False
        perfect = m = 1
        while perfect < n:
            perfect = m * m
            m += 1
        return perfect == n

assert not Solution().isPerfectSquare(0)
for n in range(1, 225):
    perfect = n * n
    assert Solution().isPerfectSquare(perfect), f'for {perfect} expected True, returned False'
    assert not Solution().isPerfectSquare(perfect + 1), f'for {perfect + 1} expected False, returned True'
