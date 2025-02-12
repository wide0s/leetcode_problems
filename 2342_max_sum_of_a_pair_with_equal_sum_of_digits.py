from collections import defaultdict

class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(log(d))
        def dig10sum(d):
            a = 0
            while d > 0:
                a += d % 10
                d //= 10
            return a
        v = -1
        d = defaultdict(int)
        for n in nums:
            k = dig10sum(n)
            if k in d:
                if d[k] + n > v:
                    v = d[k] + n
                if d[k] < n:
                    d[k] = n
            else:
                d[k] = n
        return v

vectors = [
        [18,43,36,13,7], 54,
        [10,12,19,14], -1,
        [229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401], 973,
        [179, 56, 595,343,443,1,5,493,603,5,6,78], 0
        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    expected = vectors[i+1]
    print(f'{nums}, expected {expected}')
    returned = Solution().maximumSum(nums)
    assert expected == returned, f'for {nums} expected {expected}, but returned {returned}!'
