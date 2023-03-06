from src.domain.board import Board


class Repository:
    def __init__(self):
        self.__board = None
        self.__last_move = None

    def save_board(self, board: Board):
        """
        Functions that saves a board to the repo.
        :param board: The board to be saved.
        :return: -
        """
        self.__board = board

    def save_move(self, move):
        """
         Functions that saves a move to the repo.
         :param board: The move to be saved.
         :return: -
         """
        self.__last_move = move

    def get_last_move(self):
        """
          Functions that returns the last move added to the repo.
          :return: None if there is no move, the last move if there are moves in the repo.
          """
        return self.__last_move

    def get_last_board(self):
        """
        Functions that returns the last board added to the repo.
        :return: None if there is no board, the last board if there are boards in the repo.
        """
        return self.__board


