struct direction {
    short di;
    short dj;
};

static struct direction directions[] = {
    {-1,-1}, {-1,0}, {-1,1}, {0,-1}, {0,1}, {1,-1}, {1,0}, {1,1}
};

static int neighbors(int** board, int rows, int cols, int i, int j) {
    int count, i2, j2, k;
    for (k = count = 0; k < sizeof(directions)/sizeof(directions[0]); k++) {
        i2 = i + directions[k].di;
        j2 = j + directions[k].dj;
        if ((i2 >= 0 && i2 < rows) && (j2 >=0 && j2 < cols))
            count += (board[i2][j2] & 0x1);
    }
    return count;
}

void gameOfLife(int** board, int boardSize, int* boardColSize) {
    int neigh, i, j;

    if (!board || !boardSize || !(*boardColSize))
        return;

    for (i = 0; i < boardSize; i++) {
        for (j = 0; j < *boardColSize; j++) {
            neigh = neighbors(board, boardSize, *boardColSize, i, j);
            if (board[i][j] == 1) {
                if (neigh == 2 || neigh == 3)
                    board[i][j] = (1 << 1) | board[i][j];
            } else if (neigh == 3) {
                board[i][j] = 1 << 1;
            }
        }
    }

    for (i = 0; i < boardSize; i++) {
        for (j = 0; j < *boardColSize; j++) {
            board[i][j] = board[i][j] >> 1;
        }
    }
}
