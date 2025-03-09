class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #causes memory limit exceeded ???
        #d = 0
        #for n in range(1, num):
        #    if num % n == 0:
        #        d += n
        #return num == d

        # see https://en.wikipedia.org/wiki/Perfect_number
        return num in { 33550336, 8128, 496, 28, 6 }

vectors = [
        33550336, True,
        30402457, False,
        8128, True,
        496, True,
        64, False,
        28, True,
        7, False,
        6, True,
        1, False
        ]

for i in range(0, len(vectors), 2):
    num = vectors[i]
    expected = vectors[i + 1]
    print(f'is_perfect_number({num}) = {expected}')
    returned = Solution().checkPerfectNumber(num)
    assert returned == expected, f'for {num} expected {expected}, returned {returned}!'
