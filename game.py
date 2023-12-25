import random


def play_round(user_choice, computer_choice):
    user_choice = user_choice.lower()
    computer_choice = computer_choice.lower()

    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "You win!"
    elif user_choice == "paper" and computer_choice == "rock":
        return "You win!"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "You win!"
    else:
        return "You lose!"


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def play_game():
    print("Welcome to Rock, Paper, Scissors")
    print("Please choose one of the following:")
    print("Rock")
    print("Paper")
    print("Scissors")

    user_choice = input("Please enter your choice: ")
    computer_choice = get_computer_choice()

    print("The computer chose: " + computer_choice)

    result = play_round(user_choice, computer_choice)
    print(result)

    play_again = input("Would you like to play again? (y/n): ")
    play_again = play_again.lower()

    if play_again == "y":
        play_game()
    else:
        print("Goodbye!")


play_game()
