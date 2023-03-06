from src.domain.board import Board


class Console:
    def __init__(self, service):
        self.__service = service

    @staticmethod
    def print_columns():
        print(" 1  " + "2  " + "3  " + "4  " + "5  ")

    @staticmethod
    def print_info():
        print("Some info related to the game.")
        print("The game is played on a 5 x 5 board.")
        print("The rows are numbered from 1 to 5 and the columns from 1 to 5.")
        print("The first player that manages to connect for of his pieces wins.")
        print("You will be player 1 and the AI will be player 2.")
        print("Have fun!")

    def check_for_win(self, all_moves, current_board):
        if self.__service.get_last_move() is not None:
            if self.__service.check_win_condition(current_board, self.__service.get_last_move(), 1):
                return True
            if self.__service.check_win_condition(current_board, self.__service.get_last_move(), 2):
                return True
            if len(all_moves) == 0:
                return True
        return False

    def game_loop(self):
        self.__service.save_board(Board())

        player = True
        ai = False
        game_progress = True
        turn = True
        total_moves = 0
        depth = 7

        while game_progress:
            current_board = self.__service.get_current_board()
            all_moves = self.__service.get_all_moves(current_board)
            self.print_columns()
            print(current_board)

            if total_moves > 6:
                depth = 8

            if total_moves >= 15:
                depth = 25

            if self.check_for_win(self.__service.get_all_moves(current_board), current_board):
                game_progress = False

            if turn == player and len(all_moves) > 0:
                while True:
                    player_input = input("Choose a column from 1 to 5: ")
                    if self.__service.check_user_input(player_input) is False:
                        print("Invalid Input!")
                    else:
                        move = self.__service.make_move(current_board, int(player_input), 1)

                        if move is False:
                            print("Invalid Move! ")
                        else:

                            self.__service.save_move(int(player_input))
                            self.__service.save_board(move)
                            total_moves += 1
                            turn = not turn
                            break

            elif turn == ai and len(self.__service.get_all_moves(current_board)) > 0:
                if len(all_moves) == 1:
                    move = self.__service.make_move(current_board, int(all_moves[0]), 2)
                    self.__service.save_move(int(all_moves[0]))
                    self.__service.save_board(move)
                    total_moves += 1
                else:
                    minmax_res = self.__service.get_best_move(current_board, depth, 0, 0, 0)
                    move = self.__service.make_move(current_board, int(minmax_res[1]), 2)

                    if move is not False:
                        self.__service.save_move(int(minmax_res[1]))
                        self.__service.save_board(move)
                        total_moves += 1
                    else:
                        move = self.__service.make_move(current_board, int(all_moves[0]), 2)
                        self.__service.save_move(int(all_moves[0]))
                        self.__service.save_board(move)
                        total_moves += 1

                turn = not turn

            current_board = self.__service.get_current_board()
            if self.check_for_win(self.__service.get_all_moves(current_board), current_board):
                game_progress = False

    def start_game(self):
        self.print_info()

        self.game_loop()

        print(self.__service.get_current_board())
        if self.__service.check_win_condition(self.__service.get_current_board(), self.__service.get_last_move(), 1):
            print("You won!")
        elif self.__service.check_win_condition(self.__service.get_current_board(), self.__service.get_last_move(), 2):
            print("You lost!")
        else:
            print("Draw!")
