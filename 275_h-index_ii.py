class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        lo, hi = 0, n
        while lo < hi:
            mid = (hi + lo) // 2
            if citations[mid] < n - mid:
                lo = mid + 1
            else:
                hi = mid
        return n - lo


vectors = [
        [100], 1,
        [1,2,100], 2,
        [0,1,3,5,6], 3,
        [1,1,3], 1,
        [0,1,3,3,3,5,6], 3,
        [0,0,0,1,2], 1,
        [0,0,0,0,2], 1,
        [11,15], 2,
        [0,0,0,0], 0
        ]

for i in range(0, len(vectors), 2):
    citations = vectors[i]
    expected = vectors[i + 1]
    print(f'{citations} h-index {expected}')
    returned = Solution().hIndex(citations)
    assert expected == returned, f'for {citations} expected {expected}, but returned {returned}!'
