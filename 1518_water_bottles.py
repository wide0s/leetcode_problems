class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        assert numExchange != 1, 'infinite number of bottles!'
        drunk_bottles = numBottles
        while (numBottles >= numExchange):
            drunk_bottles += (numBottles // numExchange)
            numBottles = (numBottles % numExchange) + (numBottles // numExchange)
        return drunk_bottles

vectors = [
        [1, 2], 1,
        [2, 2], 3,
        [3, 2], 5,
        [9, 3], 13,
        [15, 4], 19
        ]

for i in range(0, len(vectors), 2):
    params = vectors[i]
    expected = vectors[i + 1]
    print(f'{params} {expected}')
    returned = Solution().numWaterBottles(*params)
    assert returned == expected, f'for {params} expected {expected}, returned {returned}!'
