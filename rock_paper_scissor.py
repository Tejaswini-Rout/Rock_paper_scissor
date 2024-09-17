import random

def print_welcome_message():
    print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
          + "Rock vs Paper -> Paper wins \n"
          + "Rock vs Scissors -> Rock wins \n"
          + "Paper vs Scissors -> Scissors wins \n")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice:\n 1 - Rock\n 2 - Paper\n 3 - Scissors\n"))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Please enter a valid choice (1, 2, or 3).")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

def get_choice_name(choice):
    return {1: 'Rock', 2: 'Paper', 3: 'Scissors'}[choice]

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "DRAW"
    elif (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 1):
        return 'Paper'
    elif (user_choice == 1 and comp_choice == 3) or (user_choice == 3 and comp_choice == 1):
        return 'Rock'
    elif (user_choice == 2 and comp_choice == 3) or (user_choice == 3 and comp_choice == 2):
        return 'Scissors'

def play_game():
    print_welcome_message()

    while True:
        user_choice = get_user_choice()
        user_choice_name = get_choice_name(user_choice)

        print('User choice is:', user_choice_name)
        print("Now it's Computer's Turn...")

        comp_choice = random.randint(1, 3)
        comp_choice_name = get_choice_name(comp_choice)

        print("Computer choice is:", comp_choice_name)
        print(user_choice_name, 'vs', comp_choice_name)

        result = determine_winner(user_choice, comp_choice)

        if result == "DRAW":
            print("<== It's a tie! ==>")
        elif result == user_choice_name:
            print("<== User wins! ==>")
        else:
            print("<== Computer wins! ==>")

        if input("Do you want to play again? (Y/N): ").strip().lower() == 'n':
            break

    print("Thanks for playing!")

# Start the game
play_game()
