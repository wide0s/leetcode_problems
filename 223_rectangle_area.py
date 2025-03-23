class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        S1 = (ax2 - ax1) * (ay2 - ay1)
        S2 = (bx2 - bx1) * (by2 - by1)
        if ax2 <= bx1 or ax1 >= bx2 or by2 <= ay1 or by1 >= ay2:
            return S1 + S2
        S3 = (min(ax2, bx2) - max(ax1, bx1)) * (min(ay2, by2) - max(ay1, by1))
        return S1 + S2 - S3

vectors = [
        -3, 0, 3, 4, 0, -1, 9, 2, 45,
        -2, -2, 2, 2, -2, -2, 2, 2, 16,
        -5, 4, 0, 5, -3, -3, 3, 3, 41
        ]

for i in range(0, len(vectors), 9):
    ax1 = vectors[i]
    ay1 = vectors[i + 1]
    ax2 = vectors[i + 2]
    ay2 = vectors[i + 3]
    bx1 = vectors[i + 4]
    by1 = vectors[i + 5]
    bx2 = vectors[i + 6]
    by2 = vectors[i + 7]
    expected = vectors[i + 8]
    print(f'({ax1}, {ay1}), ({ax2}, {ay2}), ({bx1}, {by1}), ({bx2}, {by2}) -> {expected}')
    returned = Solution().computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
    assert expected == returned, f'for <({ax1},{ay1}), ({ax2}, {ay2})> and <({bx1},{by1}), ({bx2}, {by2})> expected {expected}, but returned {returned}!'
