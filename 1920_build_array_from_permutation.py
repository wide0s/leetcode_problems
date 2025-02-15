class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        for i in range(0, len(nums)):
            ans[i] = nums[nums[i]]
        return ans

vectors = [
        [0,2,1,5,3,4], [0,1,2,4,5,3],
        [5,0,1,2,3,4], [4,5,0,1,2,3]
        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    print(nums)
    expected = vectors[i+1]
    returned = Solution().buildArray(nums)
    assert expected == returned, f'for {nums} expected {expected}, but returned {returned}!'
