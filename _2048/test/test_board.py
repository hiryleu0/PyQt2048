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
