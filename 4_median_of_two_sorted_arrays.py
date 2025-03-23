# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
#
# Constraints:
#  nums1.length == m
#  nums2.length == n
#  0 <= m <= 1000
#  0 <= n <= 1000
#  1 <= m + n <= 2000
#  -106 <= nums1[i], nums2[i] <= 106

class Solution(object):
    def medianOf(self, arr):
        if len(arr) == 0:
            return 0
        idx = (len(arr) - 1) // 2
        if len(arr) % 2 == 0:
            return (arr[idx] + arr[idx + 1]) / 2.
        return arr[idx]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0 and len(nums2) == 1:
            return nums2[0]
        if len(nums2) == 0 and len(nums1) == 1:
            return nums1[0]
        return self.medianOf(sorted(nums1 + nums2))
# COULDN'T SOLVE FOR O(log(n + m)) !

vectors = [
    [2, 2, 4, 4], [2, 2, 2, 4, 4], 2.0,
]

for i in range(0, len(vectors), 3):
    nums1 = vectors[i]
    nums2 = vectors[i + 1]
    expected = vectors[i + 2]
    print(f'{nums1} {nums2} {expected}')
    returned = Solution().findMedianSortedArrays(nums1, nums2)
    assert expected == returned, f'for nums1 = {nums1} nums2 = {nums2} expected {expected}, returned {returned}!'
