# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element
# appears only once. The relative order of the elements should
# be kept the same. Then return the number of unique elements
# in nums.
#
# Consider the number of unique elements of nums to be k, to get
# accepted, you need to do the following things:
#
#   Change the array nums such that the first k elements of nums
#   contain the unique elements in the order they were present in
#   nums initially. The remaining elements of nums are not important
#   as well as the size of nums.
#
#   Return k.
#
# Constraints:
#  1 <= nums.length <= 3 * 104
#  -100 <= nums[i] <= 100
#  nums is sorted in non-decreasing order.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        k, j = 0, 1
        while j < n:
            if nums[j] <= nums[k]:
                j += 1
                continue
            nums[k + 1], nums[j] = nums[j], nums[k + 1]
            k, j = k + 1, j + 1
        return k + 1

vectors = [
        [1], 1,
        [1,1], 1,
        [1,2], 2,
        [1,1,1], 1,
        [1,2,2], 2,
        [1,1,2], 2,
        [1,2,2], 2,
        [1,2,3], 3,
        [0,0,1,1,1,2,2,3,3,4], 5,
        [0,1,2,3,4,5,6,7,8,9], 10,
        [1,2,3,3,3], 3,
        [1,2,3,4,4], 4,
        [1,2,3,4,5], 5,
        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    print(f'{nums}')
    expected = vectors[i+1]
    returned = Solution().removeDuplicates(nums)
    assert expected == returned, f'for {nums} expected {expected}, but returned {returned}!'
