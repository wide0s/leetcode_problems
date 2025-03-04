class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

vectors = [
        [7,1,5,3,6,4], 7,
        [1,2,3,4,5], 4,
        [7,6,4,3,1], 0,
        [9,3,8,5,7,1,9,2,3,4,5,6,7,8,9], 22,
        [7,4,9,7,7,4,3,4,1,6], 11,
        [10,3,14,18,18,6,18,7,15,5,8,5,18,13,20,10,3,2,18,5], 74
        ]

for i in range(0, len(vectors), 2):
    prices = vectors[i]
    expected = vectors[i + 1]
    print(f'{prices} max profit {expected}')
    returned = Solution().maxProfit(prices)
    assert expected == returned, f'for {prices} expected max profit {expected}, returned {returned}!'
