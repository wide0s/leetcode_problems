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

assert Solution().missingNumber([9,6,4,2,3,5,7,0,1]) == 8
