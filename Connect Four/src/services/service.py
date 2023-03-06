from src.domain.board import Board
import copy


class Service:
    """
    Service layer class.
    """
    def __init__(self, repository):
        self.__repository = repository
        self.__checker = CheckInput

    def check_user_input(self, user_input):
        """
        Function that checks the user input.
        :param user_input: The user input string.
        :return: True if the input is valid, False otherwise.
        """
        return self.__checker.check_column_input(user_input)

    def get_current_board(self):
        """
        Functions that returns the last board saved in the repository.
        :return: The last board object saved in the repository.
        """
        return self.__repository.get_last_board()

    @staticmethod
    def make_move(board, column, piece):
        """
        Functions that makes a move on a board object, and returns a new board object.
        :param board: the board object.
        :param column: the column where the move must be made.
        :param piece: the piece that will be moved.
        :return: a new board with said changes.
        """
        current_board = board.board

        smallest_row = -1
        for row in range(5):
            if current_board[row][column - 1] == 0:
                smallest_row = row

        if smallest_row == -1 or column == 0:
            return False

        board.set_element(smallest_row, column - 1, piece)
        return board

    @staticmethod
    def check_coordinates(row, column):
        """
        Function that checks if given coordinates are valid.
        :param row: the row coordinate.
        :param column: the column coordinate.
        :return: True if the coordinates are valid, False otherwise,
        """
        if row < 0 or column < 0:
            return False
        if row > 4 or column > 4:
            return False
        return True

    def check_win_condition(self, board_object, column, player):
        """
        Function that checks if a certain player has won the game based on the last move.
        :param board_object: the board object.
        :param column: the last move performed.
        :param player: the player's pieces.
        :return: True if the player has won the game, False otherwise.
        """
        current_board = board_object.board

        row = 0
        column -= 1
        for aux in range(5):
            if current_board[aux][column] == player:
                row = aux
                break

        if current_board[row][column] != player:
            return False

        x = row
        y = column
        counter = 1
        while self.check_coordinates(x + 1, y) and current_board[x + 1][y] == player:
            counter += 1
            x += 1

        if counter >= 4:
            return True

        x = row
        y = column
        counter = 1
        while self.check_coordinates(x, y - 1) and current_board[x][y - 1] == player:
            counter += 1
            y -= 1

        x = row
        y = column
        while self.check_coordinates(x, y + 1) and current_board[x][y + 1] == player:
            counter += 1
            y += 1

        if counter >= 4:
            return True

        x = row
        y = column
        counter = 1
        while self.check_coordinates(x - 1, y - 1) and current_board[x - 1][y - 1] == player:
            counter += 1
            x -= 1
            y -= 1

        x = row
        y = column
        while self.check_coordinates(x + 1, y + 1) and current_board[x + 1][y + 1] == player:
            counter += 1
            x += 1
            y += 1

        if counter >= 4:
            return True

        x = row
        y = column
        counter = 1
        while self.check_coordinates(x + 1, y - 1) and current_board[x + 1][y - 1] == player:
            counter += 1
            x += 1
            y -= 1

        x = row
        y = column
        while self.check_coordinates(x - 1, y + 1) and current_board[x - 1][y + 1] == player:
            counter += 1
            x -= 1
            y += 1

        if counter >= 4:
            return True
        return False

    def save_board(self, board):
        """
        Function that saves a board in the repository.
        :param board: The board to be saved.
        :return: -
        """
        self.__repository.save_board(board)

    def get_best_move(self, board_object, max_level, level, turn, prev_move):
        """
        Function that returns the best move given a current board and witch player's turn is it using minmax algorithm.
        param board_object: the current board object.
        param max_level: the max depth of the algorithm.
        param turn: 1 if it's the player's turn, 0 if it's the AI's.
        param level: the current depth of the search.
        return: a list, the first element being the "score" of the best move, and the second is the move.
        """
        if self.check_win_condition(board_object, prev_move, 1):
            return [5000, prev_move]

        if self.check_win_condition(board_object, prev_move, 2):
            return [-5000, prev_move]

        best_move = prev_move
        if turn == 0:
            result = 9999
        else:
            result = -9999

        possible_moves = copy.deepcopy(self.get_all_moves(copy.deepcopy(board_object)))

        if level == max_level or len(possible_moves) == 0:
            return [0, prev_move]

        for move in possible_moves:
            if turn == 1:
                new_board = copy.deepcopy(self.make_move(copy.deepcopy(board_object), move, 1))
            elif turn == 0:
                new_board = copy.deepcopy(self.make_move(copy.deepcopy(board_object), move, 2))

            subtree_result = self.get_best_move(new_board, max_level, level + 1, not turn, move)

            if turn == 0:
                if result == -5000:
                    break
                if subtree_result[0] < result:
                    result = subtree_result[0]
                    best_move = move
            elif turn == 1:
                if result == 5000:
                    break
                if subtree_result[0] > result:
                    result = subtree_result[0]
                    best_move = move

        return [result, best_move]

    @staticmethod
    def get_all_moves(board_object):
        """
        Function that returns all moves available on a certain board.
        :param board_object: The board object.
        :return: An array with all the possible moves.
        """
        current_board = board_object.board
        moves = []

        for column in range(5):
            if current_board[0][column] == 0:
                moves.append(int(column) + 1)

        return moves

    def save_move(self, move):
        """
        Function that saves a move in the repository.
        :param move: The move to be saved.
        :return: -
        """
        self.__repository.save_move(move)

    def get_last_move(self):
        """
        Function that returns the last move from the repository.
        :return: the last saved move.
        """
        return self.__repository.get_last_move()


class CheckInput:
    """
    Validator class.
    """
    @staticmethod
    def check_column_input(user_input):
        """
        Function that checks if a given input is a valid column or not.
        :param user_input: the user input.
        :return: True if the given input is correct, False oherwise.
        """
        try:
            user_input = int(user_input)
            if user_input < 1 or user_input > 5:
                return False
            return True
        except ValueError:
            return False
