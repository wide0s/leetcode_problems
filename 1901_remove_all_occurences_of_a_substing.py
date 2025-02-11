class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        # this works faster than KMP_matcher
        index = s.find(part)
        while index > -1 and len(s) != 0:
            s = s[:index] + s[index + len(part):len(s)]
            index = s.find(part)
        return s

vectors = [
        'daabcbaabcbc', 'abc', 'dab',
        'axxxxyyyyb', 'xy', 'ab',
        'eemckxmckx', 'emckx', '',
        '', '', '',
        'a', 'a', ''
        ]

for i in range(0, len(vectors), 3):
    s = vectors[i]
    part = vectors[i+1]
    expected = vectors[i+2]
    print(f'{s} {part}')
    returned = Solution().removeOccurrences(s, part)
    assert expected == returned, f'for {s} expected {expected}, but returned {returned}!'
