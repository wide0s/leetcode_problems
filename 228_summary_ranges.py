class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        if len(nums) > 0:
            i, j = 0, 0
            for j in range(1, len(nums)):
                if abs(nums[j] - nums[j - 1]) == 1:
                    continue
                if i == j - 1:
                    ranges.append('{}'.format(nums[i]))
                else:
                    ranges.append('{}->{}'.format(nums[i],nums[j-1]))
                i = j
            if i == j:
                ranges.append('{}'.format(nums[i]))
            else:
                ranges.append('{}->{}'.format(nums[i],nums[j]))
        return ranges

vectors = [
        [], [],
        [0], ['0'],
        [0,1,2,4,5,7], ['0->2','4->5','7'],
        [0,2,3,4,6,8,9], ['0','2->4','6','8->9'],
        [-100,-99,-98,-97,0,1,2,3,5,6,8,9,10,11,12,15], ['-100->-97','0->3','5->6','8->12','15'],
        [0,2,4,6,8,10], ['0','2','4','6','8','10']
        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    expected = vectors[i + 1]
    print(f'{nums} {expected}')
    returned = Solution().summaryRanges(nums)
    assert expected == returned, f'for {nums} expected {expected}, returned {returned}!'
