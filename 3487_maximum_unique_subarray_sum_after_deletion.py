class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sset = set()
        ssum, mmax = 0, -100
        for x in nums:
            if x >= 0 and x not in sset:
                sset.add(x)
                ssum += x
            if x > mmax:
                mmax = x
        return ssum if len(sset) > 0 else mmax

vectors = [
        [1,2,3,4,5], 15,
        [1,1,0,1,1], 1,
        [1,2,-1,-2,1,0,-1], 3,
        [-100], -100
        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    expected = vectors[i + 1]
    print(f'{nums} {expected}')
    returned = Solution().maxSum(nums)
    assert expected == returned, f'for {nums} expected {expected}, returned {returned}!'
