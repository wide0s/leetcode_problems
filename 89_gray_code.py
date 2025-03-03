from math import pow

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 2^n = 1 << n
        return [ x ^ (x >> 1) for x in range(1 << n) ]


vectors = [
        4, [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8],
        3, [0, 1, 3, 2, 6, 7, 5, 4],
        2, [0, 1, 3, 2],
        1, [0, 1]
        ]
for i in range(0, len(vectors), 2):
    n = vectors[i]
    expected = vectors[i + 1]
    print(f'n = {n}, gray seq {expected}')
    returned = Solution().grayCode(n)
    print('  ' + ' '.join('{0:0b}'.format(x) for x in returned))
    assert returned == expected, f'for {n} gray code {expected}, returned {returned}!'
