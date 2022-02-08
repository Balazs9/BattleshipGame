import random
from random import randint
from termcolor import colored


class Game:
    """
    Main Game area, set up the board size,
    place of the ships, player name
    """

    def __init__(self, size, number_of_ships, player_name, game_turn):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.number_of_ships = number_of_ships
        self.player_name = player_name
        self.game_turn = game_turn

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def player_guess(self):
        ship_in_row = random.randint(0, 9)
        ship_in_col = random.randint(0, 9)
        player_number_row = int(input("Hit a number between 0 and 9:"))
        player_number_col = int(input("Hit a number between 0 and 9:"))

        for game_turn in range(5):
            print("Game on", game_turn+1)
            print(colored("Don't forget to choose a number between 0 and 9"))

            try:
                while(player_number_row != ship_in_row and player_number_col != ship_in_col):
                    print(f"Try again")
                    player_number_row = int(input("Hit a number between 0 and 9:"))
                    player_number_col = int(input("Hit a number between 0 and 9:"))

                    if (player_number_row == ship_in_row and player_number_col == ship_in_col):
                        print("Well done, you hit it")
                        print("Game Finished")
            except ValueError as e:
                print(f"Sorry {e} is not a number, you must enter a number")
                return False


def new_game():
    size = 9
    game_turn = 5
    number_of_ships = 5
    player_name = input("Please enter your name:")
    game = Game(size, number_of_ships, player_name, game_turn)
    game.print_board()
    game.player_guess()


new_game()
