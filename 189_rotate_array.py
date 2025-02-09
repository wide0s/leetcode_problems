# Given an integer array nums, rotate the array to the right
# by k steps, where k is non-negative.
# 
# Constraints:
#  1 <= nums.length <= 105
#  -231 <= nums[i] <= 231 - 1
#  0 <= k <= 105

# Brian W. Kernighan and P. J. Plauger, "Software Tools in Pascal", p.194-195,
#  https://seriouscomputerist.atariverse.com/media/pdf/book/Software%20Tools%20in%20Pascal.pdf
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        def reverse(a, i, j=None):
            j = len(a) - 1 if j is None else j
            while i < j:
                a[i], a[j] = a[j], a[i]
                i, j = i + 1, j - 1

        def rotate(a, k):
            n = len(a)
            if n > 1 and k > 0 and k % n != 0:
                j = n - 1 - k % n
                if j >= 0:
                    reverse(a, 0, j)
                    reverse(a, j + 1)
                    reverse(a, 0)

        rotate(nums, k)

vectors = [
        [], 2, [],
        [1], -4, [1],
        [1], 0, [1],
        [1], 1, [1],
        [0,1,2,3,4], 1, [4,0,1,2,3],
        [0,1,2,3,4], 2, [3,4,0,1,2],
        [0,1,2,3,4], 3, [2,3,4,0,1],
        [0,1,2,3,4], 4, [1,2,3,4,0],
        [0,1,2,3,4], 5, [0,1,2,3,4],
        [0,1,2,3,4], 1 + 7770, [4,0,1,2,3],
        [0,1,2,3,4], 2 + 1789670, [3,4,0,1,2],
        [0,1,2,3,4], 3 + 785, [2,3,4,0,1],
        [0,1,2,3,4], 4 + 452625, [1,2,3,4,0],
        [0,1,2,3,4], 5 + 987 * 5, [0,1,2,3,4],
        [0,1,2,3,4], 2, [3,4,0,1,2],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14], 5 + 10000 * 14, [10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]
        ]

for i in range(0, len(vectors), 3):
    a = vectors[i]
    nums = [ e for e in a ]
    k = vectors[i+1]
    print(f'{a}, k={k}')
    expected = vectors[i+2]
    Solution().rotate(nums, k)
    assert expected == nums, f'for {a} and k {k} expected {expected}, but returned {nums}!'
