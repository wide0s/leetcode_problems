import copy

class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image)
        if n == 1:
            image[0][0] = 1 - image[0][0]
            return image
        m = n // 2
        for i in range(n):
            for j in range(m):
                a = image[i][j]
                image[i][j] = 1 - image[i][n - j - 1]
                image[i][n - j - 1] = 1 - a
            if n % 2 != 0:
                image[i][j + 1] = 1 - image[i][j + 1]
        return image

vectors = [
        [[0]], [[1]],
        [[1, 0], [1, 0]], [[1, 0], [1, 0]],
        [[1,1,0], [1,0,1], [0,0,0]], [[1,0,0], [0,1,0], [1,1,1]],
        [[1,1,0,0], [1,0,0,1], [0,1,1,1],[ 1,0,1,0]], [[1,1,0,0], [0,1,1,0], [0,0,0,1], [1,0,1,0]]
]

for i in range(0, len(vectors), 2):
    matrix = copy.deepcopy(vectors[i])
    expected = vectors[i + 1]
    print(matrix)
    returned = Solution().flipAndInvertImage(vectors[i])
    assert expected == returned, f'for {matrix} expected {expected}, returned {returned}'
