class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        assert 2 <= k <= 10
        assert n >= 0
        a = 0
        while n > 0:
            a += n % k
            n //= k
        return a

vectors = [
        0, 5, 0,
        34, 6, 9,
        10, 10, 1
        ]

for i in range(0, len(vectors), 3):
    n = vectors[i]
    k = vectors[i+1]
    print(f'n={n} k={k}')
    expected = vectors[i+2]
    returned = Solution().sumBase(n, k)
    assert expected == returned, f'for n={n} and k={k} expected {expected}, but returned {returned}!'
