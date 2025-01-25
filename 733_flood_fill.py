# You are given an image represented by an m x n grid of integers image, where image[i][j]
# represents the pixel value of the image. You are also given three integers sr, sc, and color.
# Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].
#
# To perform a flood fill:
#  1. Begin with the starting pixel and change its color to color.
#  2. Perform the same process for each pixel that is directly adjacent
#     (pixels that share a side with the original pixel, either horizontally or vertically)
#     and shares the same color as the starting pixel.
#  3. Keep repeating this process by checking neighboring pixels of the updated pixels and
#     modifying their color if it matches the original color of the starting pixel.
#  4. The process stops when there are no more adjacent pixels of the original color to update.
#
# Return the modified image after performing the flood fill.

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        assert sr >= 0 and sr < len(image)
        assert sc >= 0 and sc < len(image[0])

        def fill(image, i, j, original_color, color):
            n, m = len(image), len(image[0])
            if image[i][j] == color or image[i][j] != original_color:
                return
            image[i][j] = color
            if i - 1 >= 0 and image[i - 1][j] == original_color:
                fill(image, i - 1, j, image[i - 1][j], color)
            if i + 1 < n and image[i + 1][j] == original_color:
                fill(image, i + 1, j, image[i + 1][j], color)
            if j + 1 < m and image[i][j + 1] == original_color:
                fill(image, i, j + 1, image[i][j + 1], color)
            if j - 1 >= 0 and image[i][j - 1] == original_color:
                fill(image, i, j - 1, image[i][j - 1], color)

        fill(image, sr, sc, image[sr][sc], color)
        return image

vectors = [
    [[1,1,1], [1,1,0], [1,0,1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]], 
    [[1,1,1], [1,1,1]], 0, 0, 1, [[1,1,1], [1,1,1]]
]

for i in range(0, len(vectors), 5):
    image = vectors[i]
    sr = vectors[i + 1]
    sc = vectors[i + 2]
    color = vectors[i + 3]
    expected = vectors[i + 4]
    filled = Solution().floodFill(image, sr, sc, color)
    assert image == filled, f'for {image} expecting {expected}, but got {filled}'
