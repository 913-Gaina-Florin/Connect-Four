import unittest

from src.domain.board import Board


class BoardTest(unittest.TestCase):
    def test(self):
        board = Board()

        self.assertEqual(board.board, [
            [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
        ])

        board.set_element(0, 0, 1)
        new_board = Board()
        new_board.board = board

        self.assertEqual(board.board,  [
            [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
        ])

        self.assertRaises(ValueError, board.set_element, 0, -1, 1)

        self.assertEqual(str(board), "[1, 0, 0, 0, 0]\n[0, 0, 0, 0, 0]\n[0, 0, 0, 0, 0]\n[0, 0, 0, 0, 0]\n[0, 0, 0, 0, 0]\n")


