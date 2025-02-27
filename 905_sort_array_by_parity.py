class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(nums, key = lambda n: n % 2 != 0)

vectors = [
        [3,1,2,4], [2,4,3,1],
        [5,2,1,4,3,6,8,11], [2,4,6,8,5,1,3,11]
        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    print(nums)
    expected = vectors[i + 1]
    returned = Solution().sortArrayByParity(nums)
    assert expected == returned, f'for {nums} expected {expected}, returned {returned}!'
