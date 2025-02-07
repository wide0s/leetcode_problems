class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

vectors = [
        [1,2,2,1],[2,2],[2],
        [4,9,5],[9,4,9,8,4],[9,4]
        ]

for i in range(0, len(vectors), 3):
    nums1 = vectors[i]
    nums2 = vectors[i+1]
    expected = vectors[i+2]
    returned = Solution().intersection(nums1, nums2)
    assert expected == returned, f'for {nums1} and {nums2} expected {expected}, but returned {returned}!'
