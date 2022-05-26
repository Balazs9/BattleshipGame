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
        self.player = []
        self.computer = []
        self.ship_in_row = random.randint(0, self.size)
        self.ship_in_col = random.randint(0, self.size)
        print(self.ship_in_row)
        print(self.ship_in_col)

    def print_board(self):
        """
        Print the game area
        """
        for row in self.board:
            print(" ".join(row))

    def player_guess(self):
        """
        Player guess the ship coordinates
        Validator check if the given value is a number
        if it is in the given range
        """
        for game_turn in range(7):
            try:
                print("Game", game_turn + 1)
                player_guess_row = int(input("row: \n"))
                player_guess_col = int(input("column: \n"))
                if(player_guess_row == self.ship_in_row and player_guess_col == self.ship_in_col):
                    self.player.append((player_guess_row, player_guess_col))
                    self.board[player_guess_row][player_guess_col] = "*"
                    self.print_board()
                    print(colored(f"Great job {self.player_name}, you found the ship", "yellow"))
                    break
                else:
                    try:
                        self.player.append((player_guess_row, player_guess_col))
                        self.board[player_guess_row][player_guess_col] = "P"
                        print(colored("------------------", "red"))
                        self.print_board()
                        print(colored("------------------", "red"))
                        print(colored("Sorry wrong, try an other number!", "yellow"))
                    except IndexError:
                        print(colored(f"Please enter a number between 0 and {self.size}!", "red"))
                self.computer_guess()
                game_turn += 1
            except ValueError as e:
                print(f"Sorry {e} is not a number, you must enter a number!")
        if game_turn == 7:
            print(colored("Game Over", "blue"))

    def computer_guess(self):
        """
        Computer guess, random numbers
        Validator checks if the random number is a number
        if it is in the given range
        """
        def computer_number():
            return randint(0, self.size)

        comp_row = computer_number()
        comp_col = computer_number()  
        try:
            if(comp_row == self.ship_in_row and comp_col == self.ship_in_col):
                self.computer.append((comp_row, comp_col))
                self.board[comp_row][comp_col] = "@"
                self.print_board()
                print(colored("Great, you found the ship", "green"))
            else:
                try:
                    self.computer.append((comp_row, comp_col))
                    self.board[comp_row][comp_col] = "C"
                    print(colored("------------------", "red"))
                    self.print_board()
                    print(colored("------------------", "red"))
                    print(colored("Sorry wrong, try an other number!", "green"))
                except IndexError:
                    print(colored(f"Please enter a number between 0 and {self.size}!", "red"))
        except ValueError as e:
            print(f"Sorry {e} is not a number!")


def new_game():
    """
    new game is calling the game functions
    player able to customize the grid size
    display the game rules
    giving colors for the player and the computer
    """
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
    print(colored("Player against the computer", "yellow"))
    print(colored("Each the player and the computer has 7 chance to guess the place of the ship", "yellow"))
    print(colored("The range for the numbers to chhose is between 0 and 8", "yellow"))
    print(colored("The player neer to pick a number for the row and a number for the column too", "yellow"))
    print(colored("validator checking if the given guesses are correct", "yellow"))
    print(colored("To set the size of the board, please enter a number", "yellow"))
    print(colored("Please enter your name and give the number for the board size", "yellow"))
    # player giving their name
    player_name = input(colored("Please enter your name: ", "red"))
    # while loop with isaplha() method, to check the given name is valid
    while not player_name.isalpha():
        # if player type nothing or a number it will be invalid
        print("Sorry invalid name, please try again!")
        player_name = input(colored("Please enter your name: ", "red"))

    size = 20
    number_of_ships = size/2
    game_turn = 7
    print(colored(f"Hi {player_name}, enjoy the fight", "yellow"))
    print(colored("*" * 35, "red"))
    game = Game(size, number_of_ships, player_name, game_turn)
    game.print_board()
    game.player_guess()
    game.computer_guess()


new_game()
