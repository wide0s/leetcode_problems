class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def sum_digits(number):
            tot = 0
            while number > 0:
                tot += number % 10
                number //= 10
            return tot
        v = num
        while v > 9:
            v = sum_digits(v)
        return v

vectors = [
        38, 2,
        0, 0
        ]

for i in range(0, len(vectors), 2):
    num = vectors[i]
    expected = vectors[i+1]
    returned = Solution().addDigits(num)
    assert expected == returned, f'for {num} expected {expected}, but returned {returned}!'
