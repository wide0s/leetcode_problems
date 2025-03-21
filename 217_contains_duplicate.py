class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

vectors = [
        [1,2,3,1], True,
        [1,2,3,4], False,
        [1,1,1,3,3,4,3,2,4,2], True
        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    expected = vectors[i + 1]
    print(f'{nums} {expected}')
    returned = Solution().containsDuplicate(nums)
    assert expected == returned, f'for {nums} expected {expected}, returned {returned}!'
