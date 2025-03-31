# FROM https://www.geeksforgeeks.org/edit-distance-dp-5/
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def editDistRec(s1, s2, m, n, memo):
            if m == 0:
                return n
            if n == 0:
                return m
            if memo[m][n] != -1:
                return memo[m][n]
            if s1[m - 1] == s2[n - 1]:
                memo[m][n] = editDistRec(s1, s2, m - 1, n - 1, memo)
                return memo[m][n]
            memo[m][n] = 1 + min(editDistRec(s1, s2, m, n - 1, memo),
                                 editDistRec(s1, s2, m - 1, n, memo),
                                 editDistRec(s1, s2, m - 1, n - 1, memo))
            return memo[m][n]

        m, n = len(word1), len(word2)
        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        return editDistRec(word1, word2, len(word1), len(word2), memo)

vectors = [
    ['horse', 'ros'], 3,
    ['intention', 'execution'], 5
]

for i in range(0, len(vectors), 2):
    params = vectors[i]
    expected = vectors[i + 1]
    print(f'{params} {expected}')
    returned = Solution().minDistance(*params)
    assert expected == returned, f'for {params} expected {expected}, returned {returned}!'
