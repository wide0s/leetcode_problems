class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def parse_complex(s):
            im, re = 0, 0
            seen_plus = False
            buf = ''
            for c in s:
                if c == ' ':
                    continue
                elif c == '+':
                    seen_plus = True
                    # case: '4+...'
                    if len(buf) > 0: re = int(buf)
                    buf = ''
                    continue
                elif not seen_plus and c == '-':
                    # case: '-1i'
                    if len(buf) > 1: re = int(buf)
                    buf = '-'
                    continue
                elif c == 'i':
                    if len(buf) == 0:
                        # case: 'i'
                        im = 1
                    elif len(buf) == 1 and buf[0] == '-':
                        # case: '-i'
                        im = -1
                    else:
                        # cases: '-4i', '54i'
                        im = int(buf)
                    buf = ''
                    break
                buf = buf + c
            if len(buf) > 0:
                # case: purue real number
                re = int(buf)
            #print(f'{(re, im)} \'{buf}\'')
            return re, im

        re1, im1 = parse_complex(num1)
        re2, im2 = parse_complex(num2)

        # complex multiplication
        re3 = re1*re2 - im1*im2
        im3 = re1*im2 + im1*re2

        return str(re3) + '+' + str(im3) + 'i'

vectors = [
        'i', 'i', '-1+0i',
        '-i', '-i', '-1+0i',
        '-2i', '2i','4+0i',
        '-2i', '+2i','4+0i',
        '1', '1', '1+0i',
        '1+1i', '1+1i', '0+2i',
        '1+-1i', '1+-1i', '0+-2i',
        '1+0i', '1+0i', '1+0i',
        '1+-5i', '2+4i', '22+-6i',
        ]

for i in range(0, len(vectors), 3):
    num1 = vectors[i]
    num2 = vectors[i+1]
    print(f'({num1}) * ({num2})')
    expected = vectors[i+2]
    returned = Solution().complexNumberMultiply(num1, num2)
    assert expected == returned, f'for ({num1}) * ({num2}) expected {expected}, but returned {returned}'
