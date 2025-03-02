class Solution(object):
    def stringHash(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        o = ''
        for i in range(0, len(s), k):
            hv = 0
            for j in range(i, i + k):
                hv += ord(s[j]) - ord('a')
            o += chr(hv % 26 + ord('a'))
        return o

vectors = [
        'a', 1, 'a',
        'abcd', 2, 'bf',
        'mxz', 3, 'i',
        ]

for i in range(0, len(vectors), 3):
    s = vectors[i]
    k = vectors[i + 1]
    expected = vectors[i + 2]
    print(f'{s}, k={k}')
    returned = Solution().stringHash(s, k)
    assert expected == returned, f'for {s} and {k} expected {expected}, returned {returned}!'
