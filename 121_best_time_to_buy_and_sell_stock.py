# You are given an array prices where prices[i] is the price
# of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day 
# to buy one stock and choosing a different day in the future
# to sell that stock.
#
# Return the maximum profit you can achieve from this
# transaction. If you cannot achieve any profit, return 0.
#
# Constraints:
#
#  1 <= prices.length <= 10^5
#  0 <= prices[i] <= 10^4

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = max(profit, price - min_price)
        return profit

vectors = [
        [7,1,5,3,6,4], 5,
        [7,6,4,3,1], 0,
        [2,1,2,1,0,1,2], 2,
        [3,3,5,0,0,3,1,4], 4
        ]

for i in range(0, len(vectors), 2):
    prices = vectors[i]
    expected = vectors[i + 1]
    print(f'{prices} max profit {expected}')
    returned = Solution().maxProfit(prices)
    assert expected == returned, f'for {prices} expected {expected}, returned {returned}'
