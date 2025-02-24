class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0

        value = 0
        fsm_state = 0 # 0 - sign, 1 - digit
        sign = 1
        MAXMOD = 2**31 - 1
        for c in s:
            x = ord(c) - ord('0')
            if fsm_state == 1:
                if x < 0 or x > 9:
                    break
                n = value * 10
                if (MAXMOD - n) >= x:
                    value = n + x
                else:
                    value = MAXMOD
                    break
            else:
                if c in [' ', '\t']:
                    pass
                elif c == '-':
                    sign = -1
                    MAXMOD = 2**31
                    fsm_state = 1
                elif c == '+':
                    fsm_state = 1
                elif 0 <= x <= 9:
                    value = x
                    fsm_state = 1
                else:
                    break
        return sign * value

vectors = [
        None, 0,
        '', 0,
        '1', 1,
        '+1', 1,
        '-1', -1,
        '42', 42,
        '-42', -42,
        '-042', -42,
        '-2147483649', -2**31,
        '2147483648', 2**31 - 1,
        '  --042', 0,
        '1337c0d3', 1337,
        '0-1', 0,
        'words and 987', 0,
        '  --42', 0,
        '  -+3', 0,
        ' ++4', 0,
        '   +-65', 0
        ]

for i in range(0, len(vectors), 2):
    s = vectors[i]
    expected = vectors[i + 1]
    returned = Solution().myAtoi(s)
    print(f'\'{s}\' {expected} {returned}')
    assert expected == returned, f'for \'{s}\' expected {expected}, but returned {returned}!'
