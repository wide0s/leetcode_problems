class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for n in nums:
            x ^= n
        return x

vectors = [
        [4,1,2,1,2], 4,
        [2,2,1], 1,
        [1], 1,
        [-30000,356,12,5,12,5,356], -30000
        ]
for i in range(0, len(vectors), 2):
    nums = vectors[i]
    expected = vectors[i + 1]
    print(f'{nums} single number is {expected}')
    returned = Solution().singleNumber(nums)
    assert returned == expected, f'for {nums} expected {expected}, returned {returned}!'
