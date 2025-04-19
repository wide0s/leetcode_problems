class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = { 'R': 1, 'L': -1 }
        l = n = 0
        for c in s:
            l += d[c]
            if l == 0:
                n += 1
        return n

vectors = [
        'RLRRLLRLRL', 4,
        'RLRRRLLRLL', 2,
        'LLLLRRRR', 1,
        'LRLLRRRRRLLL', 3
        ]

for i in range(0, len(vectors), 2):
    s = vectors[i]
    expected = vectors[i + 1]
    print(f'{s} {expected}')
    returned = Solution().balancedStringSplit(s)
    assert returned == expected, f'for {s} expected {expected}, returned {returned}!'
