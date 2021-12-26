from random import shuffle


class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]

    def generate_random_two(self):
        xs = [x for x in range(self.size)]
        ys = [y for y in range(self.size)]
        shuffle(xs)
        shuffle(ys)
        shuffle(ys)

        for x in xs:
            for y in ys:
                if self.board[x][y] == 0:
                    self.board[x][y] = 2
                    return x, y

        return -1, -1

    def is_move_possible(self, c) -> bool:
        increasing = c < 2
        columns = c % 2 == 0

        for i in range(self.size):
            # checking if blocks can be moved without merging
            j = 0 if increasing else self.size - 1
            while 0 <= j < self.size and \
                    ((columns and self.board[j][i] != 0) or (not columns and self.board[i][j] != 0)):
                j = j + 1 if increasing else j - 1
            while 0 <= j < self.size and \
                    ((columns and self.board[j][i] == 0) or (not columns and self.board[i][j] == 0)):
                j = j + 1 if increasing else j - 1
            if 0 <= j < self.size:
                return True

            # checking if any two blocks can be merged
            for j in range(self.size - 1):
                if (columns and self.board[j][i] == self.board[j + 1][i] != 0) \
                        or (not columns and self.board[i][j] == self.board[i][j + 1] != 0):
                    return True
        return False

    def make_move(self, c):
        increasing = c < 2
        columns = c % 2 == 0

        moved = False

        for i in range(self.size):
            j = 0 if increasing else self.size - 1
            while 0 <= j < self.size:
                k = j + 1 if increasing else j - 1
                if (columns and self.board[j][i] == 0) or (not columns and self.board[i][j] == 0):
                    while 0 <= k < self.size \
                            and ((columns and self.board[k][i] == 0) or (not columns and self.board[i][k] == 0)):
                        k = k + 1 if increasing else k - 1
                else:
                    while 0 <= k < self.size and \
                            ((columns and self.board[k][i] != self.board[j][i]) or
                             (not columns and self.board[i][k] != self.board[i][j])):
                        k = k + 1 if increasing else k - 1

                if 0 <= k < self.size:
                    moved = True
                    if columns:
                        old_value = self.board[j][i]
                        self.board[j][i] = self.board[j][i] + self.board[k][i]
                        self.board[k][i] = 0
                    else:
                        old_value = self.board[i][j]
                        self.board[i][j] = self.board[i][j] + self.board[i][k]
                        self.board[i][k] = 0

                if 0 > k or k >= self.size or old_value != 0:
                    j = (j + 1 if increasing else j - 1)

        return moved

    def is_lost(self):
        return not (self.is_move_possible(0) or self.is_move_possible(1)
                    or self.is_move_possible(2) or self.is_move_possible(3))

    def is_won(self, win_value):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] >= win_value:
                    return True
        return False
