from math import pow, sqrt, fabs

# gradient descent, took it from 
# here https://github.com/doocs/leetcode/blob/main/solution/1500-1599/1515.Best%20Position%20for%20a%20Service%20Centre/README_EN.md
class Solution(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        n = len(positions)
        # calcualte the center of mass and use it as an initial guess
        x = y = 0
        for x1, y1 in positions:
            x += x1
            y += y1
        x, y = x / n, y / n
        decay = 0.999
        eps = 1e-6
        alpha = 0.5
        while 1:
            grad_x = grad_y = 0
            dist = 0
            for x1, y1 in positions:
                a = x - x1
                b = y - y1
                c = sqrt(a * a + b * b)
                grad_x += a / (c + 1e-8)
                grad_y += b / (c + 1e-8)
                dist += c
            dx = grad_x * alpha
            dy = grad_y * alpha
            x -= dx
            y -= dy
            alpha *= decay # while approaching to the minima we reducing learnig rate to increase accuracy
            if abs(dx) <= eps and abs(dy) <= eps:
                return dist

vectors = [
        [[0,1], [1,0], [1,2], [2,1]], 4.0,
        [[1,1], [3,3]], 2.82843,
        [[1,1], [0,0], [2,0]], 2.73205,
        [[44,23],[18,45],[6,73],[0,76],[10,50],[30,7],[92,59],[44,59],[79,45],[69,37],[66,63],[10,78],[88,80],[44,87]],499.28078
        ]

for i in range(0, len(vectors), 2):
    positions = vectors[i]
    print(positions)
    expected = vectors[i + 1]
    returned = Solution().getMinDistSum(positions)
    assert fabs(expected - returned) <= pow(10, -5), f'for {positions} expected {expected}, but returned {returned}!'
