import random
from random import randint
from termcolor import colored

ship_in_row = random.randint(0, 8)
ship_in_col = random.randint(0, 8)


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
        self.ship_in_row = random.randint(0, 9)
        self.ship_in_col = random.randint(0, 9)

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
        for game_turn in range(7):
            try:
                print("Game", game_turn + 1)
                player_guess_row = int(input("row: \n"))
                player_guess_col = int(input("column: \n"))
                if(player_guess_row == ship_in_row and player_guess_col == ship_in_col):
                    self.player.append((player_guess_row, player_guess_col))
                    self.board[player_guess_row][player_guess_col] = "*"
                    self.print_board()
                    print(colored("Great, you found the ship", "yellow"))
                    break
                else:
                    try:
                        self.player.append((player_guess_row, player_guess_col))
                        self.board[player_guess_row][player_guess_col] = "P"
                        self.print_board()
                        print(colored("Sorry wrong, try an other number!", "yellow"))
                    except IndexError:
                        print(colored("Please enter a number between 0 and 9!", "red"))
                    self.computer_guess()
                game_turn += 1
            except ValueError as e:
                print(f"Sorry {e} is not a number, you must enter a number!")
            if game_turn == 7:
                print(colored("Game Over", "blue"))

    def computer_guess(self):
        """
        Computer guess, random numbers
        """
        def computer_number():
            return randint(0, 9)  

        comp_row = computer_number()
        comp_col = computer_number()      
        try:
            if(comp_row == ship_in_row and comp_col == ship_in_col):
                self.computer.append((comp_row, comp_col))
                self.board[comp_row][comp_col] = "@"
                self.print_board()
                print(colored("Great, you found the ship", "green"))
            else:
                try:
                    self.computer.append((comp_row, comp_col))
                    self.board[comp_row][comp_col] = "C"
                    self.print_board()
                    print(colored("Sorry wrong, try an other number!", "green"))
                except IndexError:
                    print(colored("Please enter a number between 0 and 9!", "red"))
        except ValueError as e:
            print(f"Sorry {e} is not a number!")

    def turn_guess(self, game_turn):
        """
        Game turn, 5 chance for each player to guess
        """
        for game in game_turn:
            if game == 5:
                print("Game over")
            else:
                game += 1


def new_game():
    """
    new game is calling the game functions
    """
    size = 9
    game_turn = 7
    number_of_ships = 5
    print(colored("      * ", "yellow"))
    print(colored("      ***** ", "yellow"))
    print(colored("      *   *  ", "yellow"))
    print(colored("      *   *  ", "yellow"))
    print(colored("*     *   *    *", "yellow"))
    print(colored(" **************", "yellow"))
    print(colored("  ************", "yellow"))
    print(colored("   **********", "yellow"))
    print(colored("*" * 35, "blue"))
    print(colored("*" * 35, "blue"))
    print(colored("*" * 35, "blue"))
    print(colored("*" * 35, "red"))
    print(colored("Game Rules: ", "yellow"))
    print(colored("9x9 matrix", "yellow"))
    print(colored("Player against the computer", "yellow"))
    print(colored("Each the player and the computer has 5 chance to guess the place of the ship", "yellow"))
    print(colored("validator checking if the given guesses are correct"))
    player_name = input(colored("Please enter your name: ", "red"))
    print(colored(f"Hi {player_name}, enjoy the fight", "yellow"))
    game = Game(size, number_of_ships, player_name, game_turn)
    game.print_board()
    game.player_guess()
    game.computer_guess()


new_game()
