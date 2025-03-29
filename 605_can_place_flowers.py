class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(0, len(flowerbed)):
            left = flowerbed[i - 1] if i > 0 else 0
            right = flowerbed[i + 1] if i + 1 < len(flowerbed) else 0
            if left == flowerbed[i] == right == 0:
                flowerbed[i] = 1
                n -= 1
        return n < 1

vectors = [
    [[0,1,0], 1], False,
    [[1,0,0,0,1], 1], True,
    [[1,0,0,0,1], 2], False,
    [[1,0,0,0,0,1], 2], False,
    [[1,0,0,0,0,0,1], 2], True
]

for i in range(0, len(vectors), 2):
    params = vectors[i]
    expected = vectors[i + 1]
    print(f'{params} {expected}')
    returned = Solution().canPlaceFlowers(*params)
    assert expected == returned, f'for {params} expected {expected}, returned {returned}!'

