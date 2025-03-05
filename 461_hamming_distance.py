class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')

vectors = [
        1, 4, 2,
        3, 1, 1,
        1577962638, 1727613287, 16
        ]

for i in range(0, len(vectors), 3):
    x = vectors[i]
    y = vectors[i + 1]
    expected = vectors[i + 2]
    print(f'hamming_distance({x}, {y}) = {expected}')
    returned = Solution().hammingDistance(x, y)
    assert expected == returned, f'for {x} and {y} expected Hamming distance {expected}, returned {returned}!'
