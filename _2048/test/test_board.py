import unittest

from _2048.board import Board


class TestBoard(unittest.TestCase):
    def test_impossible_move_when_empty_board(self):
        board = Board(3)
        self.assertEqual(board.is_move_possible(0), False)
        self.assertEqual(board.is_move_possible(1), False)
        self.assertEqual(board.is_move_possible(2), False)
        self.assertEqual(board.is_move_possible(3), False)

    def test_full_board_with_no_moves(self):
        board = Board(3)
        board.board = [
            [2, 4, 8],
            [4, 8, 16],
            [16, 32, 64],
        ]
        self.assertEqual(board.is_move_possible(0), False)
        self.assertEqual(board.is_move_possible(1), False)
        self.assertEqual(board.is_move_possible(2), False)
        self.assertEqual(board.is_move_possible(3), False)

    def test_blocks_possible_to_move_every_direction(self):
        board = Board(3)
        board.board = [
            [0, 0, 0],
            [0, 2, 0],
            [0, 0, 0],
        ]
        self.assertEqual(board.is_move_possible(0), True)
        self.assertEqual(board.is_move_possible(1), True)
        self.assertEqual(board.is_move_possible(2), True)
        self.assertEqual(board.is_move_possible(3), True)

    def test_blocks_possible_to_move_some_direction(self):
        board = Board(3)
        board.board = [
            [8, 4, 0],
            [4, 2, 0],
            [0, 0, 0],
        ]
        self.assertEqual(board.is_move_possible(0), False)
        self.assertEqual(board.is_move_possible(1), False)
        self.assertEqual(board.is_move_possible(2), True)
        self.assertEqual(board.is_move_possible(3), True)

    def test_full_board_with_merge_moves(self):
        board = Board(3)
        board.board = [
            [8, 4, 4],
            [4, 2, 2],
            [16, 16, 8],
        ]
        self.assertEqual(board.is_move_possible(0), False)
        self.assertEqual(board.is_move_possible(1), True)
        self.assertEqual(board.is_move_possible(2), False)
        self.assertEqual(board.is_move_possible(3), True)

    def test_make_move_on_empty_board(self):
        board = Board(3)
        expected_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        board.make_move(0)
        self.assertEqual(board.board, expected_board)

    def test_make_move(self):
        board = Board(3)
        initial_board = [[0, 0, 0], [0, 2, 0], [0, 0, 0]]
        board.board = initial_board
        expected_boards = [
            [[0, 2, 0], [0, 0, 0], [0, 0, 0]],
            [[2, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [2, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 2]],
        ]
        for i in range(4):
            board.make_move(i)
            self.assertEqual(board.board, expected_boards[i])

    def test_make_move_2(self):
        board = Board(3)
        initial_board = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        board.board = initial_board
        expected_boards = [
            [[4, 4, 4], [2, 2, 2], [0, 0, 0]],
            [[8, 4, 0], [4, 2, 0], [0, 0, 0]],
        ]
        for i in range(2):
            board.make_move(i)
            self.assertEqual(board.board, expected_boards[i])

    def test_make_move_3(self):
        board = Board(4)
        initial_board = [[0, 0, 0, 0], [2, 2, 2, 4], [0, 2, 2, 2], [0, 2, 2, 2]]
        board.board = initial_board
        expected_boards = [
            [[2, 4, 4, 4], [0, 2, 2, 4], [0, 0, 0, 0], [0, 0, 0, 0]],
            [[2, 8, 4, 0], [4, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [2, 8, 0, 0], [4, 4, 4, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, 8], [0, 0, 4, 8]],
        ]
        for i in range(4):
            board.make_move(i)
            self.assertEqual(board.board, expected_boards[i])

    def test_is_won(self):
        board = Board(3)
        board.board = [
            [0, 2, 4],
            [2, 4, 0],
            [16, 32, 64]
        ]
        self.assertTrue(board.is_won(32))
        self.assertTrue(board.is_won(64))
        self.assertFalse(board.is_won(128))

    def test_is_lost(self):
        board = Board(3)
        board.board = [
            [4, 2, 4],
            [2, 4, 2],
            [16, 32, 64]
        ]
        self.assertTrue(board.is_lost())

    def test_is_not_lost(self):
        board = Board(3)
        board.board = [
            [4, 2, 4],
            [2, 4, 4],
            [16, 32, 64]
        ]
        self.assertFalse(board.is_lost())

    def test_generate_random_two_on_empty_board(self):
        board = Board(3)
        board.generate_random_two()
        zeros = 0
        twos = 0
        for i in range(board.size):
            for j in range(board.size):
                if board.board[i][j] == 0:
                    zeros = zeros + 1
                elif board.board[i][j] == 2:
                    twos = twos + 1
        self.assertEqual(zeros, board.size * board.size - 1)
        self.assertEqual(twos, 1)

    def test_generate_random_two_with_one_empty_slot(self):
        board = Board(3)
        specific_board = [
            [2, 0, 4],
            [4, 8, 16],
            [16, 32, 2],
        ]
        expected_board = [
            [2, 2, 4],
            [4, 8, 16],
            [16, 32, 2],
        ]
        board.board = specific_board
        board.generate_random_two()
        self.assertEqual(board.board, expected_board)

    def test_generate_random_two_on_full_board(self):
        board = Board(3)
        full_board = [
            [4, 8, 16],
            [16, 32, 64],
            [32, 64, 128],
        ]
        board.board = full_board
        board.generate_random_two()
        self.assertEqual(board.board, full_board)
