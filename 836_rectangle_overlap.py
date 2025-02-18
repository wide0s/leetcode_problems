class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return not (rec1[2] <= rec2[0] or \
                rec1[0] >= rec2[2] or \
                rec2[3] <= rec1[1] or \
                rec2[1] >= rec1[3])

vectors = [
        [0,0,2,2], [1,1,3,3], True,
        [0,0,1,1], [1,0,2,1], False,
        [0,0,1,1], [2,2,3,3], False
        ]

for i in range(0, len(vectors), 3):
    rec1 = vectors[i]
    rec2 = vectors[i + 1]
    print(f'{rec1} {rec2}')
    expected = vectors[i + 2]
    returned = Solution().isRectangleOverlap(rec1, rec2)
    assert expected == returned, f'for {rec1} and {rec2} expected {expected}, but returned {returned}!'
