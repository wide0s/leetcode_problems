# Given an unsorted integer array nums. Return the smallest
# positive integer that is not present in nums.
#
# You must implement an algorithm that runs in O(n) time and
# uses O(1) auxiliary space.
#
# Constraints:
#  1 <= nums.length <= 105
#  -231 <= nums[i] <= 231 - 1
#
# FROM https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/

class Solution(object):
    # runtime complexity is O(n), beats 55%
    # sapce complexity is O(1)
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        # using the cyclic sort
        for i in range(n):
            # swap[i] a and a[a[i] - 1] so that a[i] is
            # at its index
            while 1 <= a[i] <= n and a[i] != a[a[i] - 1]:
                t = a[i]
                a[i] = a[a[i] - 1]
                a[t - 1] = t
        # go through to find the first one which is not
        # at its index
        for i in range(n):
            if a[i] != i + 1:
                # found the first one, which is not at its
                # index, so return it
                return i + 1
        # all numbers are their indices, so return n + 1
        return n  + 1

vectors = [
        [-1], 1,
        [0], 1,
        [1], 2,
        [2], 1,
        [-2,0], 1,
        [-2,1], 2,
        [-2,2], 1,
        [3,4,0,10,1,-10,5,-1], 2,
        [1,2,0], 3,
        [2,1,0], 3,
        [3,4,-1,1], 2,
        [7,8,9,11,12], 1,
        [1,2,3,4,5], 6,
        [-1,4,2,1,9,10], 3
        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    print(nums)
    expected = vectors[i+1]
    returned = Solution().firstMissingPositive(nums)
    assert expected == returned, f'for {nums} expected {expected}, but returned {returned}!'
