# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the
# index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Constraints:
#  1 <= nums.length <= 104
#  -104 <= nums[i] <= 104
#  nums contains distinct values sorted in ascending order.
#  -104 <= target <= 104

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def bisection(a, target, left=0, right=None):
            assert left >= 0
            assert not right or right >= 0
            if not right:
                right = len(a)
            while left < right:
                mid = (right + left) // 2
                if a[mid] < target:
                    left = mid + 1
                elif a[mid] > target:
                    right = mid
                else:
                    return mid
            return left # instead of -1

        return bisection(nums, target)

vectors = [
        [1,3,5,6], 5, 2,
        [1,3,5,6], 2, 1,
        [1,3,5,6], 7, 4,
        [1,3,5,6], 0, 0,
        ]

for i in range(0, len(vectors), 3):
    nums = vectors[i]
    target = vectors[i+1]
    print(f'{nums}, target={target}')
    expected = vectors[i+2]
    returned = Solution().searchInsert(nums, target)
    assert expected == returned, f'for {nums} and target {target} expected {expected}, but returned {returned}!'
