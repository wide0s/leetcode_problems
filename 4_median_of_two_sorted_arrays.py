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
    def medianOf(self, arr, start=0, end=None):
        if end == None:
            end = len(arr) - 1
        llen = end - start + 1
        assert llen > 0
        idx = start + (llen - 1) // 2
        if llen % 2 == 0:
            return idx, (arr[idx] + arr[idx + 1]) / 2.
        else:
            return idx, arr[idx]
        

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

Solution().findMedianSortedArrays([2,2,4,4], [2,2,2,4,4])
