class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return False

        fsm_state = 0 # 0 - sign { {+, -} (0..1) || digit (0..*) || . (0..1) },
                      # 1 - number { digit (0..*) || . (0.. 1) || {e, E} (0..1) }
        exp = False
        dot = False
        signs = [False, False]
        digits = [0, 0]
        digidx = 0 
        for c in s:
            x = ord(c) - ord('0')
            if fsm_state == 1:
                if not exp and c in 'eE':
                    exp = True
                    digidx = 1
                    dot = True # exponent is always an integer
                    fsm_state = 0
                elif not dot and c == '.':
                    dot = True
                elif 0 <= x <= 9:
                    digits[digidx] += 1
                else:
                    return False
            elif fsm_state == 0:
                if c in '-+':
                    signs[digidx] = True
                    fsm_state = 1
                elif 0 <= x <= 9:
                    digits[digidx] += 1
                    fsm_state = 1
                elif not dot and c == '.':
                    dot = True
                    fsm_state = 1
                else:
                    return False
        if (exp and digits[1] == 0) or (dot and digits[0] == 0) \
                or (signs[0] and digits[0] == 0):
            return False
        return True

vectors = [
        None, False,
        "", False,
        ".", False,
        "e", False,
        "+", False,
        "-", False,
        "-e", False,
        ".e1", False,
        "2", True,
        "0089", True,
        "-0.1", True,
        "+3.14", True,
        "4.", True,
        "-9.", True,
        "2e10", True,
        "-90E3", True,
        "3e+7", True,
        "+6e-1", True,
        "53.5e93", True,
        "-123.456e789", True,
        "abc", False,
        "1a", False,
        "1e", False,
        "e3", False,
        "99e2.5", False,
        "--6", False,
        "-+3", False,
        "95a54e53", False
        ]

for i in range(0, len(vectors), 2):
    s = vectors[i]
    expected = vectors[i + 1]
    print(f'{s}')
    returned = Solution().isNumber(s)
    assert expected == returned, f'for \'{s}\' expected {expected}, but returned {returned}!'
