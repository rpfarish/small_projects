import random

last_game_comp = 0


# Function prints 27 new lines
def print_new_lines():
    return print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


# Function prints 27 new lines, 100 times
def print_many_new_lines():
    for i in range(100):
        print_new_lines()


# Starts a new game, either against a person or a computer
def start():
    starting = input("Enter comp to play a computer or "
                     "Enter other to play against another player: ").lower()

    # Restarts a new game without needing to re-input the opponent parameter
    def restart():
        # Prompts user if they want to restart the game
        start_over = input("Do you want to play again?\n y or n: ").lower()
        if start_over == "y" or start_over == "yes":
            # Checks if game is initial iteration and starts the correct version
            if last_game_comp == 1:
                start_comp()
            elif last_game_comp == 2:
                start_player()
        # If input is neither y nor n, it quits the game
        else:
            print("Bye!")
            quit()

    # Starts the game against the computer
    def start_comp():
        global last_game_comp
        # Initializes that the game that was selected will restart the correct version when it is restarted
        last_game_comp = 1
        # Initializes that the game will not continue until the user enters a valid input for their choice
        confirm = False
        comp = ""
        choice = ""
        # Loops until user enters a valid input
        while not confirm:
            # Prompts a user for a choice
            choice = input("Enter Rock, Paper or Scissors: ").title()
            # If the input was Rock, Paper or Scissors then it breaks out of the loop
            if choice == "Rock" or choice == "Paper" or choice == "Scissors":
                confirm = True
            # If the input was not Rock, Paper or Scissors then it prompts the user again
            else:
                print("Please enter a valid input")

        # Generates a random number from 1 to 3
        rand = random.randrange(1, 4)
        # Assigns the random number to a choice: Rock, Paper or Scissors
        if rand == 1:
            comp = "Rock"
        elif rand == 2:
            comp = "Paper"
        elif rand == 3:
            comp = "Scissors"
        # Prints the users input and the computers random assignment
        print(f"You: {choice} Computer: {comp}")

        # If the users input and the computers random assignment were equal then Tie is printed
        if choice == comp:
            print("Tie!")

        # Checks all the Win conditions for the game
        elif choice == "Rock" and comp == "Scissors":
            print("You Win!")
        elif choice == "Rock" and comp == "Paper":
            print("You Lose :(")
        elif choice == "Paper" and comp == "Rock":
            print("You Win!")
        elif choice == "Paper" and comp == "Scissors":
            print("You Lose :(")
        elif choice == "Scissors" and comp == "Rock":
            print("You Lose :(")
        elif choice == "Scissors" and comp == "Paper":
            print("You Win!")

        # After the game ends prompts user if they want to play again
        restart()

    def start_player():
        global last_game_comp
        # Initializes that the game that was selected will restart the correct version when it is restarted
        last_game_comp = 2
        # Initializes that the game will not continue until both the user enters valid inputs for their choices
        confirm = False
        confirm2 = False
        choice = ""
        choice2 = ""
        while not confirm:
            choice = input("Player 1 \nEnter Rock, Paper or Scissors: ").title()
            print_many_new_lines()
            if choice == "Rock" or choice == "Paper" or choice == "Scissors":
                confirm = True
            else:
                print("Please enter a valid input")
        while not confirm2:
            choice2 = input("Player 2 \nEnter Rock, Paper or Scissors: \n\n\n\n\n\n>").title()
            if choice2 == "Rock" or choice2 == "Paper" or choice2 == "Scissors":
                confirm2 = True
            else:
                print("Please enter a valid input")

        print(f"Player 1: {choice} Player 2: {choice2}")

        if choice == choice2:
            print("Tie!")

        elif choice == "Rock" and choice2 == "Scissors":
            print("Player 1 Wins!")

        elif choice == "Rock" and choice2 == "Paper":
            print("Player 1 Loses :(")

        elif choice == "Paper" and choice2 == "Rock":
            print("Player 1 Wins!")
        elif choice == "Paper" and choice2 == "Scissors":
            print("Player 1 Loses :(")
        elif choice == "Scissors" and choice2 == "Rock":
            print("Player 1 Loses :(")
        elif choice == "Scissors" and choice2 == "Paper":
            print("Player 1 Wins!")
        restart()

    if starting == "comp":
        start_comp()
    if starting == "other":
        start_player()


start()
