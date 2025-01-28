class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        n, m = 2, len(colsum) 

        # TODO: is it possible to optimize memory footprint by reusing
        #       colsum as a row in the output matrix?
        matrix = [ [0] * m for _ in range(n) ]

        for index in range(m):
            if colsum[index] == 1:
                # core idea: distribute 1 uniformly between arrays
                if upper >= lower and upper > 0:
                    matrix[0][index] = 1
                    upper -= 1
                elif lower > upper and lower > 0:
                    matrix[1][index] = 1
                    lower -= 1
                else:
                    return []
            elif colsum[index] == 2 and upper > 0 and lower > 0:
                matrix[1][index] = matrix[0][index] = 1
                upper -= 1
                lower -= 1
            elif colsum[index] != 0:
                return []
        return [] if upper > 0 or lower > 0 else matrix

vectors = [
        2, 1, [1,1,1], [[1,1,0],[0,0,1]],
        2, 3, [2,2,1,1], [],
        5, 5, [2,1,2,0,1,0,1,2,0,1], [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]],
        4, 7, [2,1,2,2,1,1,1], []
]

for i in range(0, len(vectors), 4):
    upper = vectors[i]
    lower = vectors[i+1]
    colsum = vectors[i+2]
    expected = vectors[i+3]
    print(colsum)
    returned = Solution().reconstructMatrix(upper, lower, colsum)
    returned = [ sorted(x) for x in returned ]
    expected = [ sorted(x) for x in expected ]
    assert returned == expected, f'for upper {upper} lower {lower} colsum {colsum} expected {expected}, returned {returned}!'
