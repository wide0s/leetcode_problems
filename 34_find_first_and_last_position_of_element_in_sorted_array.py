# Given an array of integers nums sorted in non-decreasing
# order, find the starting and ending position of a given
# target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Constraints:
#  0 <= nums.length <= 105
#  -109 <= nums[i] <= 109
#  nums is a non-decreasing array.
#  -109 <= target <= 109

from bisect import bisect_left

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def first_index(a, target):
            index = bisect_left(a, target)
            if index != len(a) and a[index] == target:
                return index
            return -1

        def last_index(a, target):
            index = bisect_left(a, target + 1)
            if index < len(a) or a[index - 1] == target:
                return index - 1
            return -1

        i = first_index(nums, target)
        indices = [i] * 2
        if len(nums) > 1 and indices[0] >= 0:
            i = last_index(nums, target)
            if i > 0:
                indices[1] = i
        return indices

vectors = [
        [], 0, [-1,-1],
        [1], 1, [0,0],
        [5,7], 7, [1,1],
        [5,7,7,8,8,10,11], 8, [3,4],
        [5,7,7,8,8,10,11], 6, [-1,-1],
        [5,7,7], 7, [1,2],
        [3,3,3], 3, [0,2],
        [2,2], 2, [0,1],
        [1,2,3,4,7,7,7,7,7,7,7], 7, [4, 10]
        ]

for i in range(0, len(vectors), 3):
    nums = vectors[i]
    target = vectors[i+1]
    print(f'{nums}, target={target}')
    expected = vectors[i+2]
    returned = Solution().searchRange(nums, target)
    assert expected == returned, f'for {nums} and target {target} expected {expected}, but returned {returned}!'
