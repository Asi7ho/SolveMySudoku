import numpy as np


class Solver(object):
    def __init__(self, board):
        self.lines = "012345678"
        self.columns = "012345678"

        self.board = np.zeros((9, 9))
        for key in sorted(board.keys()):
            column = int(key[0])
            line = int(key[1])
            self.board[line][column] = int(board[key])

        self.solve()

        self.values = dict()
        for l in self.lines:
            for c in self.columns:
                key = c + l
                value = self.board[int(l)][int(c)]
                self.values[key] = str(int(value))

    def possible(self, line, col, nb):
        # check column
        for j in range(9):
            if self.board[line][j] == nb:
                return False

        # check line
        for i in range(9):
            if self.board[i][col] == nb:
                return False

        # check square
        y0 = (col // 3) * 3
        x0 = (line // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[x0 + i][y0 + j] == nb:
                    return False

        return True

    def solve(self):
        for x in range(9):
            for y in range(9):
                if self.board[x][y] == 0:
                    for n in range(1, 10):
                        if self.possible(x, y, n):
                            self.board[x][y] = n
                            if self.solve():
                                return True

                            self.board[x][y] = 0
                    return False
        return True
