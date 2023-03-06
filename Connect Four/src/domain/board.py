
class Board:
    def __init__(self):
        self.__board = [
            [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
        ]

    @property
    def board(self):
        """
        Property getter that returns the __board field of the class.
        :return: the __board field of the class.
        """
        return self.__board

    @board.setter
    def board(self, new_board):
        """
        Setter for the __board field of the class.
        :param new_board: the new_board to be set.
        :return: -
        """
        self.__board = new_board

    def set_element(self, row, column, value):
        """
        Function that sets a given element of the board with a new value.
        :param row: the row of the board.
        :param column: the column of the board.
        :param value: the value of the cell.
        :return: -
        """
        if row < 0 or column < 0 or row > 4 or column > 4:
            raise ValueError("Invalid row or column!")

        self.__board[row][column] = value

    def __str__(self):
        """
        Method for converting the object to str.
        :return: The str representation of the object.
        """
        result = ""
        for i in range(len(self.__board)):
            result = result + str(self.__board[i])
            result = result + "\n"

        return result
