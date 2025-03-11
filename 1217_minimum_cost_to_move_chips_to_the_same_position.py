class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        chips_at_even_positions = sum(1 for pos in position if pos & 1 == 0)
        return min(chips_at_even_positions, len(position) - chips_at_even_positions)

vectors = [
        [1,2,3], 1,
        [2,2,2,3,3], 2,
        [1,1000000000], 1
        ]

for i in range(0, len(vectors), 2):
    position = vectors[i]
    expected = vectors[i + 1]
    print(f'{position} cost is {expected}')
    returned = Solution().minCostToMoveChips(position)
    assert returned == expected, f'for {position} expected cost is {expected}, returned {returned}!'
