class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        for x in nums:
            d = 0
            while x > 0:
                x //= 10
                d += 1
            n += (d % 2 == 0)
        return n

vectors = [
        [12], 1,
        [12,345,2,6,7896], 2,
        [555,901,482,1771], 1
        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    expected = vectors[i + 1]
    print(f'{nums} {expected}')
    returned = Solution().findNumbers(nums)
    assert expected == returned, f'for {nums} there are {expected} numbers with even numbers, returned {returned}!'
