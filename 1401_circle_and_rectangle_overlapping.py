import math

# NOT MY SOLUTION: https://www.geeksforgeeks.org/check-if-any-point-overlaps-the-given-circle-and-rectangle/
class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        # nearest point on the rectangle to the center of the circle
        x = max(x1, min(x2, xCenter))
        y = max(y1, min(y2, yCenter))
        return math.sqrt((x - xCenter)**2 + (y - yCenter)**2) <= radius


# 1: circle is above and intersection(circle, rectangle) = {(8, 4)}:
# 2: circle is below and intersection(cirlce, rectangle) = {(6, 1)}
# 3: circle to the right of the rectangle and intersection(circle, rectangle) = {(10, 3)}
# 4: circle to the left of the recangle and intersection(circle, rectangle) = {(5, 2)}
# 5: circle is inside of the rectangle and intersection(circle, rectangle) = {(6, 4), (5, 3)}
# 6: circle is inside of the rectangle and intersection(circle, rectangle) = {}
vectors = [
        2, 8, 6, 5, 1, 10, 4, True,
        1, 6, 0, 5, 1, 10, 4, True,
        2, 12, 3, 5, 1, 10, 4, True,
        3, 2, 2, 5, 1, 10, 4, True,
        1, 6, 3, 5, 1, 10, 4, True,
        0.5, 8.5, 2.5, 5, 1, 10, 4, True,
        2, 12, -1, 5, 1, 10, 4, False,
        1415, 807, -784, -733, 623, -533, 1005, False
        ]

for i in range(0, len(vectors), 8):
    radius = vectors[i]
    xCenter = vectors[i+1]
    yCenter = vectors[i+2]
    x1 = vectors[i+3]
    y1 = vectors[i+4]
    x2 = vectors[i+5]
    y2 = vectors[i+6]
    expected = vectors[i+7]
    returned = Solution().checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2)
    assert expected == returned, f'for circle (({xCenter}, {yCenter}), {radius}) and rectangle (({x1},{y1}), ({x2},{y2})) expected {expected}, but returned {returned}!'
