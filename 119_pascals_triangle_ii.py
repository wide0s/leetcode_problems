class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        n = rowIndex
        C = [1] * (n + 1)
        # C(n; k) = (n - k + 1)/k * C(n; k - 1)
        # C(n; k) = C(n; n - k)
        for k in range(1, (n // 2) + 1):
            C[k] = C[k - 1]
            C[k] *= n - k + 1
            C[k] //= k
            C[n - k] = C[k]
        return C

vectors = [
        0, [1],
        1, [1,1],
        2, [1,2,1],
        3, [1, 3, 3, 1],
        4, [1, 4, 6, 4, 1],
        33, [1, 33, 528, 5456, 40920, 237336, 1107568, 4272048, 13884156, 38567100, 92561040, 193536720, 354817320, 573166440, 818809200, 1037158320, 1166803110, 1166803110, 1037158320, 818809200, 573166440, 354817320, 193536720, 92561040, 38567100, 13884156, 4272048, 1107568, 237336, 40920, 5456, 528, 33, 1]
]

for i in range(0, len(vectors), 2):
    value = vectors[i]
    print(value)
    expected = vectors[i + 1]
    returned = Solution().getRow(value)
    assert expected == returned, f'for {value} expected {expected}, returned {returned}'
