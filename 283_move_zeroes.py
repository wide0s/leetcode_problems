class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #j = -1
        #for i in range(len(nums)):
        #    if nums[i] == 0 and (j == -1 or nums[j] != 0):
        #        j = i
        #    elif nums[i] != 0 and j != -1:
        #        nums[j], nums[i] = nums[i], 0
        #        if nums[j + 1] == 0:
        #            j += 1
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

vectors = [
    [0], [0],
    [1,2,3,4,-5], [1,2,3,4,-5],
    [0,1,2,-3,4], [1,2,-3,4,0],
    [1,2,-3,4,0], [1,2,-3,4,0],
    [1,-2,0,0,2], [1,-2,2,0,0],
    [0,1,0,3,12], [1,3,12,0,0],
    [0,0,0,0,5], [5,0,0,0,0],
    [0,1,2,3,0,4,0,5], [1,2,3,4,5,0,0,0],
    [0,0,0,1,0,0,0,0,5,0], [1,5,0,0,0,0,0,0,0,0],
    [0,0,0,1,-100,0,0,0,5,0], [1,-100,5,0,0,0,0,0,0,0],
    [1,-2,0,3,0,0,4,0,0,0,-100], [1,-2,3,4,-100,0,0,0,0,0,0],
    [1,0,0,-10,-5,0,0,0,4,5,0,0,1,0,2,3,0,0,0,9], [1,-10,-5,4,5,1,2,3,9] + [0] * 11,
]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    returned = list(nums)
    expected = vectors[i + 1]
    print(f'{nums} {expected}')
    Solution().moveZeroes(returned)
    assert expected == returned, f'for {nums} expected {expected}, returned {returned}!'
