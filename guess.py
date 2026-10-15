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