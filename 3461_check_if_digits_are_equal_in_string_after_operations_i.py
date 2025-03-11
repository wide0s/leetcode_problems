from collections import deque

class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False
        s = deque(map(int, s))
        while len(s) > 2:
            sn = deque()
            for i in range(len(s) - 1):
                sn.append((s[i] + s[i + 1]) % 10)
            s = sn
        return s[0] == s[1]

vectors = [
        '3902', True,
        '34789', False,
        '1122334455', False,
        '99', True
        ]

for i in range(0, len(vectors), 2):
    s = vectors[i]
    expected = vectors[i + 1]
    print(f'\'{s}\' {expected}')
    returned = Solution().hasSameDigits(s)
    assert returned == expected, f'for {s} expected {expected}, returned {returned}!'
