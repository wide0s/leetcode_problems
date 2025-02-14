class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        v, o = 0, []
        for n in nums:
            v = ((v << 1) + n) % 5
            o.append(v == 0)
        return o

vectors = [
        [1], [False],
        [0,1,1], [True, False, False],
        [1,1,1], [False, False, False],
        [1,0,1,0], [False, False, True, True]
        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    print(nums)
    expected = vectors[i+1]
    returned = Solution().prefixesDivBy5(nums)
    assert expected == returned, f'for {nums} expected {expected}, but returned {returned}!'
