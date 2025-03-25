class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), \
                      (0,1), (1,-1), (1,0), (1,1)]

        def neighbors(board, i, j):
            # [i-1, j-1] [i-1, j] [i-1, j+1]
            # [i  , j-1] [  i, j] [  i, j+1]
            # [i+1, j-1] [i+1, j] [i+1, j+1]
            count = 0
            for di, dj in directions:
                i2, j2 = i + di, j + dj
                if 0 <= i2 < n and 0 <= j2 < m:
                    count += board[i2][j2] & 1
            return count

        for i in range(n):
            for j in range(m):
                neigh = neighbors(board, i, j)
                if board[i][j] == 1:
                    if neigh == 2 or neigh == 3:
                        board[i][j] = (1 << 1) | board[i][j]
                elif neigh == 3:
                    board[i][j] = 1 << 1

        for i in range(n):
            for j in range(m):
                board[i][j] = board[i][j] >> 1

vectors = [
        [[0,1,0],[0,0,1],[1,1,1],[0,0,0]], [[0,0,0],[1,0,1],[0,1,1],[0,1,0]],
        [[1,1],[1,0]], [[1,1],[1,1]]
        ]

import copy
for i in range(0, len(vectors), 2):
    a = vectors[i]
    board = copy.deepcopy(a)
    expected = vectors[i + 1]
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(f'{a[i][j]} ', end='')
        print(' ->  ', end='')
        for j in range(len(expected[0])):
            print(f'{expected[i][j]} ', end='')
        print('')
    print('')
    Solution().gameOfLife(board)
    assert expected == board, f'for {a} expected {expected}, returned {board}!'
