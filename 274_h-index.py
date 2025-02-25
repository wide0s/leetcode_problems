class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        c = sorted(citations)
        H_index = 0
        for i in range(len(c)):
            x = len(c) - i
            if c[i] >= x:
                H_index = max(H_index, x)
        return H_index
       
vectors = [
        [100], 1,
        [3,0,6,1,5], 3,
        [1,3,1], 1,
        [0,1,3,3,3,5,6], 3,
        [0,0,0,1,2], 1,
        [0,0,0,0,2], 1,
        [11,15], 2,
        [0,0,0,0], 0
        ]

for i in range(0, len(vectors), 2):
    citations = vectors[i]
    print(citations)
    expected = vectors[i + 1]
    returned = Solution().hIndex(citations)
    assert expected == returned, f'for {citations} expected {expected}, but returned {returned}!'
