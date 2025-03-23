class Solution(object):
    def reverse(self, x):
        # x in [-2**31,  2**31 - 1]
        if x == -2**31:
            return 0

        sign = 1
        if x < 0:
            sign = -1
            x = -x

        max_int = 2**31 - 1
        o = 0
        while x > 0:
            r = x % 10
            if max_int // 10 < o or max_int - o * 10 < r:
                o = 0
                break
            o = o * 10 + r
            x = x // 10
            assert o <= max_int
        return o if sign > 0 else -o

vectors = [
    123, 321,
    -123, -321
]

for i in range(0, len(vectors), 2):
    x = vectors[i]
    expected = vectors[i + 1]
    print(f'{x} {expected}')
    returned = Solution().reverse(x)
    assert expected == returned, f'for x = {x} expected {expected}, returned {returned}!'
