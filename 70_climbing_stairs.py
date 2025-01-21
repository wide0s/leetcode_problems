class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        fibonachi = [1, 2]
        for i in range(2, n):
            reg = fibonachi[-1]
            fibonachi[-1] += fibonachi[-2]
            fibonachi[-2] = reg
        return fibonachi[-1]

for i in range(45):
    print(f'{i + 1} {Solution().climbStairs(i + 1)}')
    if i + 1 < 4:
         assert Solution().climbStairs(i + 1) == i + 1
