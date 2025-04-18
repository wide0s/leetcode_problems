# Given an m x n matrix, return all elements of the matrix in spiral order.
#
# Input = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# Output = [1,2,3,6,9,8,7,4,5]

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def spiral(matrix):
            rows, columns = len(matrix), len(matrix[0])
            x = y = 0 # initial cell
            while rows > 0 and columns > 0:
                i = j = 0
                # moving to the right
                if columns < 1:
                    break
                for j in range(columns):
                    yield matrix[x][y + j]
                rows -= 1
                # moving down
                if rows < 1:
                    break
                for i in range(1, rows + 1):
                    yield matrix[x + i][y + j]
                columns -= 1
                # moving to the left
                if columns < 1:
                    break
                for j in range(1, columns + 1):
                    yield matrix[x + i][y + columns - j]
                j = columns - j
                rows -= 1
                # moving up
                if rows < 1:
                    break
                for i in range(0, rows):
                    yield matrix[x + rows - i][y + j]
                i = rows - i
                columns -= 1
                # setting the initial cell [x][y]
                x += i
                y += j + 1

        return [ e for e in spiral(matrix) ]

vectors = [ 
        [[1]], [1], 
        [[1,2]], [1,2], 
        [[1], [2]], [1,2],
        [[1,2], [3,4]], [1,2,4,3],
        [[1,2,3], [4,5,6], [7,8,9]], [1,2,3,6,9,8,7,4,5], 
        [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]], [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
]
            
for i in range(0, len(vectors), 2):
    matrix = vectors[i]
    expected = vectors[i + 1]
    print(f'{matrix} {expected}')
    result = Solution().spiralOrder(matrix) 
    assert result == expected, f'for {matrix} should be {expected}, returned {result}'
