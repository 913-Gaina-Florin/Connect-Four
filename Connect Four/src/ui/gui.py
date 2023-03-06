import pygame
import sys

from src.domain.board import Board

WIDTH = 800
HEIGHT = 800

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
LN_COLOR = (23, 145, 135)
BG_COLOR = (28, 170, 156)


class GameUI:
    def __init__(self, service):
        self.__service = service

    @staticmethod
    def draw_line(screen):
        step = WIDTH // 5
        for row in range(0, WIDTH, step):
            pygame.draw.line(screen, LN_COLOR, (row, 0), (row, HEIGHT), 10)

        step = HEIGHT // 5
        for column in range(0, HEIGHT, step):
            pygame.draw.line(screen, LN_COLOR, (0, column), (WIDTH, column), 10)

    def set_up(self):
        pygame.init()

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("CONNECT FOUR")
        screen.fill(BG_COLOR)

        self.draw_line(screen)
        return screen

    @staticmethod
    def draw_image(screen, x, y, image):
        screen.blit(image, (x, y))

    def draw_board(self, screen):
        current_board = self.__service.get_current_board()
        board = current_board.board
        player1 = pygame.image.load('model1.png')
        player2 = pygame.image.load('model2.png')

        for row in range(5):
            for column in range(5):
                if board[row][column] == 1:
                    self.draw_image(screen, column * 160, row * 160, player1)
                elif board[row][column] == 2:
                    self.draw_image(screen, column * 160, row * 160, player2)

    def check_for_win(self, all_moves, current_board):
        if self.__service.get_last_move() is not None:
            if self.__service.check_win_condition(current_board, self.__service.get_last_move(), 1):
                pygame.display.set_caption("YOU WIN!")
                return True

            if self.__service.check_win_condition(current_board, self.__service.get_last_move(), 2):
                pygame.display.set_caption("YOU LOSE!")
                return True

            if len(all_moves) == 0:
                pygame.display.set_caption("DRAW!")
                return True

        return False

    def game_loop(self, screen):
        turn = True
        player = True
        ai = False
        game_progress = True
        index = WIDTH // 5
        total_moves = 0
        depth = 7

        pygame.display.update()
        self.__service.save_board(Board())

        while True:
            current_board = self.__service.get_current_board()
            all_moves = self.__service.get_all_moves(current_board)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if total_moves > 6:
                    depth = 8

                if total_moves >= 15:
                    depth = 25

                if game_progress and turn == player:
                    pygame.display.set_caption("YOUR TURN")
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN and turn == player and len(all_moves) > 0 and game_progress:
                    mouse_y = event.pos[0]
                    player_input = (mouse_y // index) + 1

                    move = self.__service.make_move(current_board, int(player_input), 1)
                    if move is not False:
                        self.__service.save_move(int(player_input))
                        self.__service.save_board(move)
                        total_moves += 1

                        self.draw_board(screen)
                        pygame.display.update()

                        turn = not turn

                current_board = self.__service.get_current_board()
                if self.check_for_win(self.__service.get_all_moves(current_board), current_board):
                    game_progress = False
                    pygame.display.update()

                if turn == ai and game_progress and len(self.__service.get_all_moves(current_board)) > 0:
                    pygame.display.set_caption("COMPUTER'S TURN")
                    pygame.display.update()

                    if len(all_moves) == 1:
                        all_moves = self.__service.get_all_moves(self.__service.get_current_board())
                        move = self.__service.make_move(current_board, int(all_moves[0]), 2)
                        self.__service.save_move(int(all_moves[0]))
                        self.__service.save_board(move)
                        total_moves += 1

                        self.draw_board(screen)
                        pygame.display.update()
                    else:
                        minmax_res = self.__service.get_best_move(current_board, depth, 0, 0, 0)
                        move = self.__service.make_move(current_board, int(minmax_res[1]), 2)

                        if move is not False:
                            self.__service.save_move(int(minmax_res[1]))
                            self.__service.save_board(move)
                            total_moves += 1

                            self.draw_board(screen)
                            pygame.display.update()
                        else:
                            all_moves = self.__service.get_all_moves(self.__service.get_current_board())
                            new_move = self.__service.make_move(current_board, int(all_moves[0]), 2)
                            self.__service.save_move(int(all_moves[0]))
                            self.__service.save_board(new_move)
                            total_moves += 1

                            self.draw_board(screen)
                            pygame.display.update()

                    turn = not turn

                current_board = self.__service.get_current_board()
                if self.check_for_win(self.__service.get_all_moves(current_board), current_board):
                    game_progress = False
                    pygame.display.update()

            pygame.display.update()

    def start_game(self):
        screen = self.set_up()
        self.game_loop(screen)
