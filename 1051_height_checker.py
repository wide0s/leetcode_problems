class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = 0
        for h, s in zip(heights, sorted(heights)):
            if h != s:
                n += 1
        return n

vectors = [
        [1,1,4,2,1,3], 3,
        [5,1,2,3,4], 5,
        [1,2,3,4,5], 0
        ]

for i in range(0, len(vectors), 2):
    heights = vectors[i]
    expected = vectors[i + 1]
    print(f'{heights} {expected}')
    returned = Solution().heightChecker(heights)
    assert returned == expected, f'for {heights} expected {expected}, returned {returned}!'
