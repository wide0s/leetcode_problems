class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        parf = lambda x: x % 2
        for i in range(len(nums)):
            nums[i] = parf(nums[i])
        return sorted(nums)

vectors = [
        [4,3,2,1], [0,0,1,1],
        [1,5,1,4,2], [0,0,1,1,1]
        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    expected = vectors[i + 1]
    print(f'{nums} {expected}')
    returned = Solution().transformArray(nums)
    assert expected == returned, f'for {nums} expected {expected}, returned {returned}!'
