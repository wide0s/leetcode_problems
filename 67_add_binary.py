class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(b) > len(a):
            a, b = b, a
        c, carry_bit = '', 0
        for i in range(len(b)):
            d = int(a[len(a) - i - 1]) + int(b[len(b) - i - 1]) + carry_bit
            carry_bit = 1 if d > 1 else 0
            c = str(d % 2) + c
        for j in range(i + 1, len(a)):
            d = int(a[len(a) - j - 1]) + carry_bit
            carry_bit = 1 if d > 1 else 0
            c = str(d % 2) + c
        return '1' + c if carry_bit == 1 else c

vectors = [
        "11", "1", "100",
        "1010", "1011", "10101",
        "1110", "11", "10001",
        "1110", "1", "1111",
        "1111", "1111", "11110",
        "10111111", "10111111101010", "11000010101001"
        ]

for i in range(0, len(vectors), 3):
    a = vectors[i]
    b = vectors[i + 1]
    print(f'a={a} b={b}')
    expected = vectors[i + 2]
    returned = Solution().addBinary(a, b)
    assert expected == returned, f'for {a} and {b} expected {expected}, but returned {returned}!'
