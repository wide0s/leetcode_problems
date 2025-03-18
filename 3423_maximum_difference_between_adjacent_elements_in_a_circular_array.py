class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distance = abs(nums[-1] - nums[0])
        for i in range(1, len(nums)):
            distance = max(distance, abs(nums[i - 1] - nums[i]))
        return distance

vectors = [
        [1,2,4], 3,
        [-5,-10,-5], 5
        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    expected = vectors[i + 1]
    print(f'{nums} {expected}')
    returned = Solution().maxAdjacentDistance(nums)
    assert expected == returned, f'for {nums} expected {expected}, returned {returned}!'
