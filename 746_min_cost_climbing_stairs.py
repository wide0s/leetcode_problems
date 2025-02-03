# You are given an integer array cost where cost[i]
# is the cost of i-th step on a staircase. Once you 
# pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or
# the step with index 1.
#
# Return the minimum cost to reach the top of the floor.
#
# Constraints:
#  2 <= cost.length <= 1000
#  0 <= cost[i] <= 999

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])

vectors = [
        [10,15,20], 15,
        [1,100,1,1,1,100,1,1,100,1], 6
        ]

for i in range(0, len(vectors), 2):
    cost = vectors[i]
    print(cost)
    expected = vectors[i+1]
    returned = Solution().minCostClimbingStairs(cost)
    assert expected == returned, f'for {cost} expected {expected}, but returned {returned}!'
