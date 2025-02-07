# Given an array of integers nums which is sorted in
# ascending order, and an integer target, write a
# function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime
# complexity.
#
# Constraints:
#  1 <= nums.length <= 104
#  -104 < nums[i], target < 104
#  All the integers in nums are unique.
#  nums is sorted in ascending order.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)
        while left < right:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return -1

vectors = [
        [1], 1, 0,
        [1], 2, -1,
        [-1,0,3,5,9,12], 9, 4,
        [-1,0,3,5,9,12], 2, -1
        ]

for i in range(0, len(vectors), 3):
    nums = vectors[i]
    print(nums)
    target = vectors[i+1]
    expected = vectors[i+2]
    returned = Solution().search(nums, target)
    assert expected == returned, f'for {nums} and target {target} expected {expected}, but returned {returned}!'
