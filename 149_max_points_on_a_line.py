from collections import defaultdict

class Line(object):
    def __init__(self, point1, point2):
        self.x1 = point1[0]
        self.y1 = point1[1]
        self.x2 = point2[0]
        self.y2 = point2[1]
        self.dx = self.x1 - self.x2
        self.dy = self.y1 - self.y2
        if self.dx == 0:
            self.k = float('inf')
            self.b = float('inf')
            self.hv = hash((self.k, self.x1))
        else:
            self.k = self.dy / float(self.dx)
            self.b = (self.x1 * self.y2 - self.y1 * self.x2) / float(self.dx)
            self.hv = hash((self.k, self.b))

    def lie(self, point):
        x = point[0]
        y = point[1]
        if (y - self.y1) * self.dx == (x - self.x1) * self.dy:
            return True
        return False

    def __eq__(self, other):
        return self.hv == other.hv

    def __hash__(self):
        return self.hv

    def __repr__(self):
        line = '[({},{}),({},{})]'.format(self.x1, self.y1, self.x2, self.y2)
        if self.k == float('inf'):
            line = '{} x={}'.format(line, self.x1)
        elif self.k == 0 and self.b == 0:
            line = '{} y=0'.format(line)
        elif self.k == 0:
            line = '{} y={}'.format(line, self.b)
        elif self.b == 0:
            line = '{} y={} * x'.format(line, self.k)
        else:
            line = '{} y={} * x + {}'.format(line, self.k, self.b)
        return line

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 3:
            return len(points)

        v, n = 0, len(points)
        for i in range(n):
            d = defaultdict(int)
            p1 = points[i]
            for j in range(i + 1, n):
                p2 = points[j]
                dx = p1[0] - p2[0]
                dy = p1[1] - p2[1]
                k, b = None, p1[0] # if dx = 0 => x = Const
                if dx != 0:
                    k = dy / float(dx)
                    b = (p1[0] * p2[1] - p1[1] * p2[0]) / float(dx)
                line = (k, b)
                #print(line)
                if line in d:
                    d[line] += 1
                else:
                    d[line] = 2
                v = max(d[line], v)
        return v

        # MY SLOW IMPLEMETATION
        #
        #v, n = 0, len(points)
        #d = defaultdict(int)
        #for i in range(n):
        #    for j in range(i + 1, n):
        #        line = Line(points[i], points[j])
        #        if line in d:
        #            continue
        #        d[line] = 2
        #        v = max(v, 2)
        #        print(line)
        #        for k in points:
        #            if k == points[i] or k == points[j]:
        #                continue
        #            if line.lie(k):
        #                d[line] += 1
        #                v = max(d[line], v)
        #return v

vectors = [
        [[1, 1], [2, 2], [3, 3]], 3,
        [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4,
        [[4,-3],[970,680],[-97,-35],[3,8],[60,253],[0,-13],[-270,-748],[-291,-165],[270,890],[90,228],[-220,-270],[-255,-118],[873,615],[-42,-175],[440,345],[4,-9],[170,27],[425,114],[56,203],[531,872],[295,480],[231,193],[291,225],[680,201],[-10,9],[-388,-230],[-385,-127],[-590,-990],[-7,-40],[308,222],[-616,-247],[-70,-283],[150,526],[77,113],[396,304],[-264,-311],[-6,-8],[-88,-147],[30,162],[49,176],[81,196],[-9,-124],[-27,-188],[-14,-67],[308,233],[413,676],[-77,33],[-177,-304],[0,-31],[472,774],[462,313],[-35,-148],[1,-2],[-440,-475],[154,153],[485,355],[-231,-47],[340,85],[-60,-111],[42,149],[-354,-598],[388,290],[44,-24],[3,-8],[510,143],[-308,-352],[-18,-156],[-21,-94],[-63,-316],[-118,-206],[0,73],[-240,-657],[-352,-393],[-531,-892],[-485,-295],[352,263],[616,393],[-154,-7],[3,4],[-5,-9],[63,230],[385,273],[-679,-425],[-595,-234],[-582,-360],[-176,-229],[770,473],[-539,-207],[-56,-229],[-236,-402],[-970,-620],[-425,-176],[240,799],[118,186],[10,-7],[-680,-263],[-5,7],[220,140],[-2,7],[-28,-121],[-300,-839],[-54,-284],[-194,-100],[-308,-87],[-3,-10],[-873,-555],[-90,-202],[-5,-4]], 16
        ]

for i in range(0, len(vectors), 2):
    points = vectors[i]
    expected = vectors[i+1]
    print('{}, expected {}'.format(points, expected))
    returned = Solution().maxPoints(points)
    assert returned == expected, 'for {} expected {}, but returned {}'.format(points, expected, returned)
