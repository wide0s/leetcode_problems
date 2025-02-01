class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for n in range(0, numRows):
            C = [1] * (n + 1)
            # C(n; k) = (n - k + 1)/k * C(n; k - 1)
            # C(n; k) = C(n; n - k)
            for k in range(1, (n // 2) + 1):
                C[k] = C[k - 1]
                C[k] *= n - k + 1
                C[k] //= k
                C[n - k] = C[k]
            triangle += [C]
        return triangle

vectors = [
        1,  [[1]],
        2,  [[1],[1,1]],
        3,  [[1],[1,1],[1,2,1]],
        4,  [[1],[1,1],[1,2,1],[1,3,3,1]],
        5,  [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]],
]

for i in range(0, len(vectors), 2):
    rows = vectors[i]
    print(rows)
    expected = vectors[i + 1]
    returned = Solution().generate(rows)
    assert expected == returned, f'for {rows} expected {expected}, returned {returned}'
