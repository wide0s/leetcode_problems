class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        words = [''] * numRows
        for i in range(0, len(s), 2*(numRows - 1)):
            for j in range(i, min(len(s), i + 2*(numRows - 1))):
                if j - i < numRows:
                    words[j - i] += s[j]
                else:
                    words[numRows - 1 - (j - i) % (numRows - 1)] += s[j]
        return ''.join(words)

    def convert_fast(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        words = [''] * numRows
        current_word = 0
        down = False
        for char in s:
            words[current_word] += char
            if current_word in [0, numRows - 1]:
                down = not down
            current_word += 1 if down else -1
        return ''.join(words)


vectors = [
    ['A', 1], 'A',
    ['PAYPALISHIRING', 3], 'PAHNAPLSIIGYIR',
    ['PAYPALISHIRING', 4], 'PINALSIGYAHRPI',
    ]

for i in range(0, len(vectors), 2):
    params = vectors[i]
    expected = vectors[i + 1]
    print(f'for {params} expected \'{expected}\'')
    returned = Solution().convert(*params)
    assert expected == returned, f'for \'{params}\' expected {expected}, but returned {returned}!'
    returned = Solution().convert_fast(*params)
    assert expected == returned, f'convert_fast(): for \'{params}\' expected {expected}, but returned {returned}!'
