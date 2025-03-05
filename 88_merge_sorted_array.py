# FROM https://leetcode.com/problems/merge-sorted-array/solutions/3958223/java-runtime-0-ms-beats-100-o-m-n/
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

vectors = [
        [4,0,0,0,0,0], 1, [1,2,3,5,6], 5, [1,2,3,4,5,6],
        [4,5,6,0,0,0], 3, [1,2,3], 3, [1,2,3,4,5,6],
        [1,4,5,0,0,0], 3, [2,3,7], 3, [1,2,3,4,5,7],
        [1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6],
        [1], 1, [], 0, [1],
        [0], 0, [1], 1, [1]
        ]

for i in range(0, len(vectors), 5):
    _nums1 = vectors[i]
    nums1 = [ x for x in _nums1 ]
    m = vectors[i + 1]
    _nums2 = vectors[i + 2]
    nums2 = [ x for x in _nums2 ]
    n = vectors[i + 3]
    expected = vectors[i + 4]
    print(f'{nums1} m = {m}, {nums2} n={n}')
    Solution().merge(nums1, m, nums2, n)
    assert expected == nums1, f'{_nums1} and m = {m}, {_nums2} and n = {n} expected {expected}, returned {nums1}!'
