import random
from random import randint
from termcolor import colored


ship_in_row = random.randint(0, 9)
ship_in_col = random.randint(0, 9)


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
        self.player = []
        self.computer = []
               
    def print_board(self):
        """
        Print the game area
        """
        for row in self.board:
            print(" ".join(row))

    def player_guess(self):
        """
        Player guess the ship coordinates
        """
        for game_turn in range(5):
            print("Game", game_turn + 1)
            player_guess_row = int(input("number: \n"))
            player_guess_col = int(input("number: \n"))
            if(player_guess_row == ship_in_row and player_guess_col == ship_in_col):
                self.player.append((player_guess_row, player_guess_col))
                self.board[player_guess_row][player_guess_col] = "*"
                self.print_board()
                print("Good")
            else:
                self.player.append((player_guess_row, player_guess_col))
                self.board[player_guess_row][player_guess_col] = "P"
                self.print_board()
                print("Wrong")
            self.computer_guess()
            game_turn += 1

    def computer_guess(self):
        """
        Computer guess, random numbers
        """
        comp_row = random.randint(0, 9)
        comp_col = random.randint(0, 9)

        if(comp_row == ship_in_row and comp_col == ship_in_col):
            self.player.append((comp_row, comp_col))
            self.board[comp_row][comp_col] = "@"
            self.print_board()
            print("Good")
        else:
            self.player.append((comp_row, comp_col))
            self.board[comp_row][comp_col] = "C"
            self.print_board()
            print("Wrong")

    def turn_guess(self, game_turn):
        """
        Game turn, 5 chance for each player to guess
        """

        for game in game_turn:
            if(game == 5):
                print("Game over")
            else:
                game += 1


def new_game():
    """
    new game is calling the game functions
    """
    size = 9
    game_turn = 5
    number_of_ships = 5
    player_name = input("Please enter your name:")
    game = Game(size, number_of_ships, player_name, game_turn)
    game.print_board()
    game.player_guess()
    game.computer_guess()


new_game()
