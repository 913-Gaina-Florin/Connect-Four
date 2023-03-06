import unittest
from src.domain.board import Board
from src.repository.repository import Repository


class RepositoryTest(unittest.TestCase):
    def test(self):
        repo = Repository()
        board = Board()

        repo.save_board(board)
        self.assertEqual(board, repo.get_last_board())

        repo.save_move(5)
        self.assertEqual(5, repo.get_last_move())