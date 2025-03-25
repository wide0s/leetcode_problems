class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        while len(a) > 1:
            b = []
            for i in range(0, len(a) // 2):
                if i % 2 == 0:
                    b.append(min(a[2*i], a[2*i + 1]))
                else:
                    b.append(max(a[2*i], a[2*i + 1]))
            a = b
        return a[0]

vectors = [
    [1,3,5,2,4,8,2,2], 1,
    [3], 3
]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    expected = vectors[i + 1]
    print(f'{nums} {expected}')
    returned = Solution().minMaxGame(nums)
    assert expected == returned, f'for {nums} expected {expected}, returned {returned}!'