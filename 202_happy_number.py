# see https://en.wikipedia.org/wiki/Happy_number
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n > 1 and n not in seen:
            seen.add(n)
            v = 0
            while n > 0:
                v += pow(n % 10, 2)
                n = n // 10
            n = v
        return n == 1

vectors = [
        1, True,
        4, False,
        5, False,
        7, True,
        10, True,
        13, True,
        19, True,
        23, True,
        28, True,
        31, True,
        32, True,
        44, True,
        49, True,
        68, True,
        70, True,
        79, True,
        82, True,
        91, True,
        94, True,
        97, True,
        100, True,
        130, True

]

for i in range(0, len(vectors), 2):
    number = vectors[i]
    expected = vectors[i + 1]
    print(f'number = {number}')
    returned = Solution().isHappy(number)
    assert expected == returned, f'for {number} expected {expected}, returned {returned}'
