import random

def display_welcome_message():
    print("_____________________________________")
    print("\n✨ Welcome everybody ✨")
    print("Are you ready to guess the number? \n")
    print("Instructions:")
    print("1. The computer will randomly choose a number between 1 and 10.")
    print("2. Your task is to guess the number.")
    print("3. You will receive hints if your guess is too high or too low.")
    print("4. You can play as many times as you want.\n")

def get_player_choice():
    while True:
        choice = input("Do you want to play (y/n)?\n").lower()
        if choice in ['y', 'n']:
            return choice
        else:
            print("Please enter 'y' to play or 'n' to quit.")

def get_player_guess():
    while True:
        try:
            guess = int(input("Please enter a number between 1 and 10: "))
            if 1 <= guess <= 10:
                return guess
            else:
                print("It's out of range. Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 10.")

def play_round():
    target_number = random.randint(1, 10)
    attempts = 0

    while True:
        guess = get_player_guess()
        attempts += 1

        if guess == target_number:
            print("Nice, your guess is right!")
            return attempts
        elif guess < target_number:
            print("It's higher.")
        else:
            print("It's lower.")

def play_game():
    total_attempts = 0
    total_successes = 0

    while True:
        choice = get_player_choice()

        if choice == 'n':
            print(f"Total attempts: {total_attempts}")
            print(f"Total successes: {total_successes}")
            print("Goodbye 👋👋")
            break
        else:
            attempts = play_round()
            total_attempts += attempts
            total_successes += 1
            print(f"Number of attempts in this round: {attempts}")
            print(f"Total attempts so far: {total_attempts}")
            print(f"Total successes so far: {total_successes}")
            print("_____________________ \n")

if __name__ == "__main__":
    display_welcome_message()
    play_game()
