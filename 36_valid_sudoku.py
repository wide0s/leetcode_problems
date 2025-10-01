class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        vertices = ((0, 0), (0, 1), (0, 2),
                    (1, 0), (1, 1), (1, 2),
                    (2, 0), (2, 1), (2, 2))
        # boxes
        for x, y in vertices:
            digits = set()
            for dx, dy in vertices:
                cell = board[3*x + dx][3*y + dy]
                if cell == '.':
                    continue
                if cell not in digits:
                    digits.add(cell)
                else:
                    return False
        # rows
        for x in range(9):
            digits = set()
            for y in range(9):
                if board[x][y] == '.':
                    continue
                if board[x][y] not in digits:
                    digits.add(board[x][y])
                else:
                    return False
        # cols
        for y in range(9):
            digits = set()
            for x in range(9):
                if board[x][y] == '.':
                    continue
                if board[x][y] not in digits:
                    digits.add(board[x][y])
                else:
                    return False
        return True

vectors = [
    [[["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]], True],
    [[["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]], False]
]

for vector in vectors:
    board = vector[0]
    expected = vector[1]
    for row in board:
        print(row)
    print(f'expected = {expected}')
    returned = Solution().isValidSudoku(board)
    assert expected == returned, f'for {board} expected {expected}, but returned {returned}!'