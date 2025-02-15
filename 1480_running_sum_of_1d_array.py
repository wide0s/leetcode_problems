class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        o = []
        v = 0
        for e in nums:
            v += e
            o.append(v)
        return o

vectors = [
        [1], [1],
        [1,2,3,4], [1,3,6,10],
        [1,1,1,1,1], [1,2,3,4,5],
        [3,1,2,10,1], [3,4,6,16,17]
        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    print(nums)
    expected = vectors[i+1]
    returned = Solution().runningSum(nums)
    assert expected == returned, f'for {nums} expected {expected}, but returned {returned}!'
