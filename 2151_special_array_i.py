class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n > 1:
            for i in range(1, n):
                if nums[i - 1] % 2 == 0 and nums[i] % 2 == 0 \
                        or nums[i - 1] % 2 != 0 and nums[i] % 2 != 0:
                    return False
        return True

vectors = [
        [1], True,
        [2,1,4], True,
        [4,3,1,6], False
        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    print(f'{nums}')
    expected = vectors[i+1]
    returned = Solution().isArraySpecial(nums)
    assert expected == returned, f'for {nums} expected {expected}, but returned {returned}!'
