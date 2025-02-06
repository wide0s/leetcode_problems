class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k, j = 0, len(nums) - 1
        while k <= j:
            if nums[k] != val:
                k += 1
                continue
            if nums[j] == val:
                j -= 1
                continue
            nums[k], nums[j] = nums[j], nums[k]
            k += 1
        return k


vectors = [
        [], 1, 0,
        [1], 2, 1,
        [1], 1, 0,
        [3,2,2,3], 3, 2,
        [3,2,2,3], 4, 4,
        [0,1,2,2,3,0,4,2], 2, 5,
        [0,1,2,2,3,0,4,2], 4, 7
        ]


for i in range(0, len(vectors), 3):
    nums = vectors[i]
    val = vectors[i+1]
    print(f'{nums}, val = {val}')
    expected = vectors[i+2]
    returned = Solution().removeElement(nums, val)
    assert expected == returned, f'for {nums} and {val} expected {expected}, but returned {returned}!'
