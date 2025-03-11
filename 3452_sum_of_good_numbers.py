class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        good_sum = 0
        for i in range(len(nums)):
            if (i - k >= 0 and nums[i] <= nums[i - k]) or \
                    (i + k < len(nums) and nums[i] <= nums[i + k]):
                continue
            good_sum += nums[i]
        return good_sum

vectors = [
        [1,3,2,1,5,4], 2, 12,
        [2,1], 1, 2
        ]

for i in range(0, len(vectors), 3):
    nums = vectors[i]
    k = vectors[i + 1]
    expected = vectors[i + 2]
    print(f'{nums}, k = {k}, sum = {expected}')
    returned = Solution().sumOfGoodNumbers(nums, k)
    assert returned == expected, f'for {nums} and k = {k} expected {expected}, returned {returned}!'
