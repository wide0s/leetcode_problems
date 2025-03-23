class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = -1
        for n in sorted(nums):
            if n - m > 1:
                return n - 1
            m = n
        return len(nums)

vectors = [
        [9,6,4,2,3,5,7,0,1], 8
        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    expected = vectors[i + 1]
    print(f'{nums} {expected}')
    returned = Solution().missingNumber(nums)
    assert expected == returned, f'for {nums} expected {expected}, returned {returned}!'
