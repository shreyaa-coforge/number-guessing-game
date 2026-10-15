import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.
valid = False
low = 1
high = 0
while not valid:
    try:
        level = int(input("Enter the level as a number:\n1. Easy \n2. Medium \n3. Hard\n"))
        if level == 1:
            high = 50
            attempt_limit = 10
            valid = True
        elif level == 2:
            high = 100
            attempt_limit = 8
            valid = True
        elif level == 3:
            high = 500
            attempt_limit = 10
            valid = True
        else:
            print("Invalid. Choose 1, 2 or 3.\n")
    except ValueError:
        print("Invalid. Enter a valid number\n")
        continue


# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.
valid_mode = False
while not valid_mode:
    try:
        mode = int(input("Enter mode: \n 1. Classic \n 2. Time Challenge\n"))

        if mode == 1 or mode == 2:
            valid_mode = True
        else:
            print("Invalid. Choose 1 or 2\n")
    except ValueError:
        print("Invalid. Enter a valid number: \n")
        continue

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.
if mode == 1:
    while not game_loop:
        try:
            guess = int(input("Guess a number: \n"))
        except ValueError:
            print("Invalid. Enter a valid number\n")
            continue
        
        if guess < low or guess > high:
            print("Invalid. Guess a number within the range\n")
            continue
        attempt += 1
        if guess == secret_number:
            print("Winner !!!!")
            game_loop = True
            game_result = "win"
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Too low!")

        if not game_loop:
            attempt_left = attempt_limit - attempt
            print(f"You have {attempt_left} attempts left")
            if attempt >= attempt_limit:
                print("Game over!! Ran out of attempts")
                game_loop = True
                game_result = "attempt"
elif mode == 2:
    while not game_loop:
        curr_time = time.time()
        time_gone = curr_time - start_time
        time_remaining = TIME_LIMIT - time_gone
        if time_remaining <= 0:
            print("Time up!! Game over!")
            game_result = "Time up"
            game_loop = True
            break
        print("Time remaining (in seconds): ", time_remaining)

        try:
            guess = int(input("Guess a number: \n"))
        except ValueError:
            print("Enter a valid number: \n")
            continue

        curr_time = time.time()
        time_gone = curr_time - start_time
        time_remaining = TIME_LIMIT - time_gone
        if time_remaining <= 0:
            print("Time up!! Game over!")
            game_result = "Time up"
            game_loop = True
            break
        if guess < low or guess > high:
            print("Enter a valid guess within the range\n")
            continue
        attempt += 1

        if guess == secret_number:
            print("Winner!!")
            game_loop = True
            game_result = "win"

        elif guess > secret_number:
            print("Too high")
        else:
            print("Too low")
        if not game_loop:
            attempt_left = attempt_limit - attempt
            print(f"You have {attempt_left} attempts left")
            if attempt >= attempt_limit:
                print("Game over!! Ran out of attempts")
                game_loop = True
                game_result = "attempt"
# ---------- End of round ----------
# Goal: show the result that matches how the round ended.
if game_result == "win":
    print(f"You guessed the correct number in {attempt} attempts")
else:
    print(f"The secret number was {secret_number}")
    if game_result == "Time up":
        print("You ran out of time")
    elif game_result == "attempt":
        print("You ranout of attempts")