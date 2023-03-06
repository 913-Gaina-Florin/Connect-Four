import unittest

from src.domain.board import Board
from src.repository.repository import Repository
from src.services.service import Service


class TestService(unittest.TestCase):
    def test(self):
        repo = Repository()
        service = Service(repo)

        self.assertEqual(service.check_user_input(5), True)

        self.assertEqual(service.check_user_input(0), False)

        self.assertEqual(service.check_user_input("abc"), False)

        board = Board()

        service.save_board(board)

        self.assertEqual(service.get_current_board(), board)

        new_board = service.make_move(board, 1, 1)

        self.assertEqual(new_board.board, [
            [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0], [1, 0, 0, 0, 0]
        ])

        new_board = service.make_move(board, 0, 1)

        self.assertEqual(new_board, False)

        self.assertEqual(service.check_coordinates(0, 0), True)
        self.assertEqual(service.check_coordinates(-1, 0), False)
        self.assertEqual(service.check_coordinates(5, 3), False)

    def test2(self):
        repo = Repository()
        service = Service(repo)
        board = Board()

        for row in range(5):
            board = service.make_move(board, 1, 1)

        new_board = service.make_move(board, 1, 1)

        self.assertEqual(new_board, False)

        service.save_move(5)

        self.assertEqual(service.get_last_move(), 5)

    def test3(self):
        repo = Repository()
        service = Service(repo)
        board = Board()

        self.assertEqual(service.get_all_moves(board), [1, 2, 3, 4, 5])

        service.make_move(board, 1, 1)
        service.make_move(board, 2, 1)
        service.make_move(board, 3, 1)
        service.make_move(board, 4, 1)

        self.assertEqual(service.check_win_condition(board, 1, 1), True)
        self.assertEqual(service.check_win_condition(board, 4, 1), True)
        self.assertEqual(service.check_win_condition(board, 5, 1), False)

    def test4(self):
        repo = Repository()
        service = Service(repo)
        board = Board()

        service.make_move(board, 1, 1)
        service.make_move(board, 1, 1)
        service.make_move(board, 1, 1)
        service.make_move(board, 1, 1)

        self.assertEqual(service.check_win_condition(board, 1, 1), True)
        self.assertEqual(service.check_win_condition(board, 2, 1), False)

    def test5(self):
        repo = Repository()
        service = Service(repo)
        board = Board()

        service.make_move(board, 1, 2)
        service.make_move(board, 1, 2)
        service.make_move(board, 1, 2)
        service.make_move(board, 1, 1)

        service.make_move(board, 2, 1)
        service.make_move(board, 2, 1)
        service.make_move(board, 2, 1)

        service.make_move(board, 3, 1)
        service.make_move(board, 3, 1)

        service.make_move(board, 4, 1)

        self.assertEqual(service.check_win_condition(board, 1, 1), True)
        self.assertEqual(service.check_win_condition(board, 4, 1), True)

    def test6(self):
        repo = Repository()
        service = Service(repo)
        board = Board()

        service.make_move(board, 4, 2)
        service.make_move(board, 4, 2)
        service.make_move(board, 4, 2)
        service.make_move(board, 4, 1)

        service.make_move(board, 3, 1)
        service.make_move(board, 3, 1)
        service.make_move(board, 3, 1)

        service.make_move(board, 2, 1)
        service.make_move(board, 2, 1)

        service.make_move(board, 1, 1)

        self.assertEqual(service.check_win_condition(board, 1, 1), True)
        self.assertEqual(service.check_win_condition(board, 4, 1), True)

    def test7(self):
        repo = Repository()
        service = Service(repo)
        board = Board()

        service.make_move(board, 1, 1)

        best_move = service.get_best_move(board, 7, 0, 0, 0)

        self.assertEqual(best_move[1], 1)






