import random

computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number (1-100): ")

    player_number = int(player_input)

    if not player_input.isdigit():
        print("Invalid Input. Try again...")
        continue

    if player_number == computer_number:
        print("You guessed it!")
        break
    elif player_number > computer_number:
        print("Too High!")
    else:
        print("Too Low!")