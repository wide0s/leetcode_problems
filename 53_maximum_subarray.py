#FROM https://leetcode.com/problems/maximum-subarray/solutions/1595195/c-python-7-simple-solutions-w-explanation-brute-force-dp-kadane-divide-conquer/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max = 0
        max_till_now = float('-inf')
        for n in nums:
            current_max = max(n, current_max + n)
            max_till_now = max(max_till_now, current_max)
        return max_till_now

vectors = [
        [-1], -1,
        [-2,1,-3,4,-1,2,1,-5,4], 6,
        [1], 1,
        [5,4,-1,7,8], 23,
        [-2,-1], -1,
        [-1,-2], -1
]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    expected = vectors[i + 1]
    print(f'{nums} {expected}')
    returned = Solution().maxSubArray(nums)
    assert expected == returned, f'for {nums} expected {expected}, returned {returned}!'

