class Solution(object):
    # runtime O(n x m) (beats ~42%), memory O(n x m) (beats 20%)
    def imageSmoother2(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        def smooth(img, i, j, n, m):
            # [i-1, j-1] [i-1, j] [i-1, j+1]
            # [i  , j-1] [  i, j] [  i, j+1]
            # [i+1, j-1] [i+1, j] [i+1, j+1]
            neighbors, aggr = 0, 0
            min_i, max_i = max(0, i - 1), min(n, i + 2)
            min_j, max_j = max(0, j - 1), min(m, j + 2)
            for i in range(min_i, max_i):
                for j in range(min_j, max_j):
                    aggr += img[i][j]
                    neighbors += 1
            return aggr // neighbors
        n, m = len(img), len(img[0])
        smoothed = [ [0] * m for _ in range(n) ]
        for i in range(n):
           for j in range(m):
               smoothed[i][j] = smooth(img, i, j, n, m)
        return smoothed

    # runtime O(n x m) (beats ~28%), memory O(1) (beats ~81%)
    def imageSmoother(self, img):
        def smooth(img, i, j, n, m):
            # [i-1, j-1] [i-1, j] [i-1, j+1]
            # [i  , j-1] [  i, j] [  i, j+1]
            # [i+1, j-1] [i+1, j] [i+1, j+1]
            neighbors, aggr = 0, 0
            min_i, max_i = max(0, i - 1), min(n, i + 2)
            min_j, max_j = max(0, j - 1), min(m, j + 2)
            for _i in range(min_i, max_i):
                for _j in range(min_j, max_j):
                    value = img[_i][_j] & 0xFF
                    aggr += value
                    neighbors += 1
            img[i][j] = aggr // neighbors if i == n - 1 and j == m - 1 \
                    else ((aggr // neighbors) << 8) | img[i][j]
            if i >= 1 and j >= 1:
                img[i - 1][j - 1] >>= 8
            if j == m - 1 and i > 0:
                img[i - 1][j] >>= 8
            if i == n - 1 and j > 0:
                img[i][j - 1] >>= 8

        n, m = len(img), len(img[0])
        for i in range(n):
           for j in range(m):
               smooth(img, i, j, n, m)
        return img

vectors = [
        [[1,1,1], [1,0,1], [1,1,1]], [[0,0,0], [0,0,0], [0,0,0]],
        [[100,200,100],[200,50,200],[100,200,100]], [[137,141,137], [141,138,141], [137,141,137]],
        [[6, 2]], [[4, 4]],
        [[1]], [[1]]
]

print('Evaluating imageSmoother2()')
for i in range(0, len(vectors), 2):
    source = vectors[i]
    expected = vectors[i + 1]
    print(source)
    smoothed = Solution().imageSmoother2(source)
    assert smoothed == expected, f'expected {expected}, returned {smoothed}'

print('Evaluating imageSmoother()')
for i in range(0, len(vectors), 2):
    source = vectors[i]
    expected = vectors[i + 1]
    print(source)
    smoothed = Solution().imageSmoother(source)
    assert smoothed == expected, f'expected {expected}, returned {smoothed}'
