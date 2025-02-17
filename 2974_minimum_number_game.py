class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a, nums = [], sorted(nums)
        for i in range(0, len(nums), 2):
            a.append(nums[i+1])
            a.append(nums[i])
        return a

vectors = [
        [5,4,2,3], [3,2,5,4],
        [2,5], [5,2]
        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    print(nums)
    expected = vectors[i+1]
    returned = Solution().numberGame(nums)
    assert expected == returned, f'for {nums} expected {expected}, but returned {returned}!'
