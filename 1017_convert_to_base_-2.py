# 0  = 0       = 0
# 1  = 1       = (-2)^0
# 2  = 110     = (-2)^2 + (-2)
# 3  = 111     = (-2)^2 + (-2) + 1
# 4  = 100     = (-2)^2
# 5  = 101     = (-2)^2 + 1
# 6  = 11010   = (-2)^4 + (-2)^3 + (-2)^1
# 7  = 11011   = (-2)^4 + (-2)^3 + (-2)^1 + 1
# 8  = 11000   = (-2)^4 + (-2)^3
# 9  = 11001   = (-2)^4 + (-2)^3 + 1
# 10 = 11110   = (-2)^4 + (-2)^3 + (-2)^2 + (-2)
# 11 = 11111   = (-2)^4 + (-2)^3 + (-2)^2 + (-2) + 1
# 12 = 11100   = (-2)^4 + (-2)^3 + (-2)^2
# 13 = 11101   = (-2)^4 + (-2)^3 + (-2)^2 + 1
# 14 = 10010   = (-2)^4 + (-2)^1
# 15 = 10011   = (-2)^4 + (-2)^1 + 1
# 16 = 10000   = (-2)^4 
# 17 = 10001   = (-2)^4 + 1
# 18 = 10110   = (-2)^4 + (-2)^2 + (-2)
# 19 = 10111   = (-2)^4 + (-2)^2 + (-2) + 1
# 20 = 10100   = (-2)^4 + (-2)^2
# 21 = 10101   = (-2)^4 + (-2)^2 + 1
# 22 = 1101010 = (-2)^6 + (-2)^5 + (-2)^3 + (-2)

# WiKi: https://en.wikipedia.org/wiki/Negative_base
class Solution(object):
    def baseNeg2(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return '0'
        v = ''
        while n != 0:
            r = n % (-2)
            n //= -2
            if r < 0:
                n += 1 # for any base
                r += 2 # r = r + 7 for base -7
            v = str(r) + v
        return v

vectors = [
        0, '0',
        1, '1',
        2, '110',
        3, '111',
        4, '100',
        5, '101',
        6, '11010',
        7, '11011',
        8, '11000',
        9, '11001',
        10, '11110',
        11, '11111',
        12, '11100',
        13, '11101',
        14, '10010',
        15, '10011',
        16, '10000',
        17, '10001',
        18, '10110',
        19, '10111',
        20, '10100',
        21, '10101',
        22, '1101010'
        ]

for i in range(0, len(vectors), 2):
    n = vectors[i]
    expected = vectors[i + 1]
    print(f'{n} is {expected}')
    returned = Solution().baseNeg2(n)
    assert expected == returned, f'for {n} expected {expected}, but returned {returned}!'
