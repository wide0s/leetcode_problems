class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        n, m = len(num1), len(num2)
        s, carry = '', 0
        for i in range(m):
            z = int(num2[m - i - 1]) + int(num1[n - i - 1]) + carry
            carry = z // 10
            s = str(z % 10) + s
        for j in range(i + 1, n):
            z = int(num1[n - j - 1]) + carry
            carry = z // 10
            s = str(z % 10) + s
        return '1' + s if carry == 1 else s

vectors = [
        "90807867589087", "989807809800978769", "989898617668567856",
        "1989905", "43430088", "45419993",
        "99", "99", "198",
        "99", "199", "298",
        "11", "123", "134",
        "456", "77", "533",
        "0", "0", "0"
        ]

for i in range(0, len(vectors), 3):
    num1 = vectors[i]
    num2 = vectors[i + 1]
    expected = vectors[i + 2]
    print(f'{num1} + {num2} = {expected}')
    returned = Solution().addStrings(num1, num2)
    assert expected == returned, f'{num1} + {num2} = {expected} != {returned}!'
