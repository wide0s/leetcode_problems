import random
import math

class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.R = radius
        self.x0 = x_center
        self.y0 = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        # r = uniform(0, self.R) -- fails test 7!
        r = math.sqrt(random.uniform(0, self.R * self.R))
        phi = random.uniform(0, 1) * 2 * math.pi
        x = r * math.cos(phi)
        y = r * math.sin(phi)
        return [self.x0 + x, self.y0 + y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

sol = Solution(1.0, 0, 0)
for i in range(3*(10**4)):
    print(sol.randPoint())
