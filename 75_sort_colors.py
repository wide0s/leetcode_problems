class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        colors = [0,0,0]
        for c in nums:
            colors[c] += 1
        start = 0
        for c in range(len(colors)):
            for i in range(start, start + colors[c]):
                nums[i] = c
            start += colors[c]

vectors = [
        [1], [1],
        [1,2], [1,2],
        [2,0,2,1,1,0], [0,0,1,1,2,2],
        [2,0,1], [0,1,2]
        ]

for i in range(0, len(vectors), 2):
    a = vectors[i]
    nums = list(a)
    expected = vectors[i + 1]
    print(f'{nums} {expected}')
    Solution().sortColors(nums)
    assert expected == nums, f'for {a} expected {expected}, returned {nums}!'
