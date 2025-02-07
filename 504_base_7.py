class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        n = abs(num)
        v = str(n % 7)
        n //= 7
        while n > 0:
            v = str(n % 7) + v
            n //= 7
        if num < 0:
            v = '-' + v
        return v

vectors = [
        0, '0',
        100, '202',
        -7, '-10',
        7*7*7*7*7, '100000',
        -7*7*7*7*7 + 1, '-66666'
        ]

for i in range(0, len(vectors), 2):
    num = vectors[i]
    print(num)
    expected = vectors[i+1]
    returned = Solution().convertToBase7(num)
    assert expected == returned, f'for {num} expected {expected}, but returned {returned}!'
