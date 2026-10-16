# Advanced Number Guessing Game

## Project Overview

The Number Guessing Game is a Python command-line application where the player tries to guess a randomly selected secret number. The player can choose a difficulty level and a game mode.

### Features

- **Easy:** Numbers from 1 to 50, with 10 attempts.
- **Medium:** Numbers from 1 to 100, with 8 attempts.
- **Hard:** Numbers from 1 to 500, with 10 attempts.
- **Classic Mode:** Guess the secret number within the available attempts.
- **Time Challenge Mode:** Guess the secret number before the time limit expires.
- **Input validation:** Rejects invalid inputs and guesses outside the selected range.
- **Feedback:** Tells the player whether a guess is too high or too low.
- **Game outcomes:** Reports a win, an exhausted attempt limit, or a timeout, and reveals the secret number when the game ends without a win.

## Technologies Used

- Python
- `random` module
- `time` module

## How to Run

1. Ensure Python 3 is installed.
2. Open a terminal in the project directory.
3. Run the game using:

   ```bash
   python3 guess.py
   ```

4. Select a difficulty level by entering `1`, `2`, or `3`.
5. Select Classic Mode (`1`) or Time Challenge Mode (`2`).
6. Enter guesses according to the selected range and follow the displayed feedback.

## Manual Test Plan

The game was tested manually using terminal inputs. A fixed secret number of `42` was used for deterministic tests where indicated. Time Challenge timeout testing used a shortened five-second limit.

| # | What I tested | What I did | Expected result | Actual result | Pass? |
|---|---|---|---|---|---|
| 1 | Guess that is too low | Set the secret to `42` and entered `20` in Easy Classic mode | Game displays "Too low!" and continues | Game displayed "Too low!" and showed 9 attempts left | Yes |
| 2 | Guess that is too high | With the secret set to `42`, entered `50` | Game displays "Too high!" and continues | Game displayed "Too high!" and showed 8 attempts left | Yes |
| 3 | Correct guess and attempt count | Entered `20`, `50`, and `42` in that order | Game reports a win after 3 valid guesses | Game reported a win in 3 attempts | Yes |
| 4 | Letters as input | Entered `abc` at the difficulty prompt | Game rejects the input and asks for a valid number | Game displayed "Invalid. Enter a valid number" and prompted again | Yes |
| 5 | Blank guess | Pressed Enter without entering a guess | Game rejects the blank input without consuming an attempt | Game displayed an invalid-input message and continued asking for guesses | Yes |
| 6 | Number below the Easy range | Selected Easy and entered `0` | Game rejects the guess because the valid range is 1–50; attempts remain unchanged | Game displayed "Invalid. Guess a number within the range" and continued | Yes |
| 7 | Number above the Easy range | Selected Easy and entered `51` | Game rejects the guess because the valid range is 1–50; attempts remain unchanged | Game displayed "Invalid. Guess a number within the range" and continued | Yes |
| 8 | Invalid inputs do not consume attempts | Entered letters, a blank entry, `0`, and `51`, followed by valid wrong guess `10` | Invalid inputs do not consume attempts; the valid wrong guess consumes one | After the invalid inputs, the game accepted `10` and displayed 9 attempts left | Yes |
| 9 | Easy difficulty and attempt limit | Selected Easy and made valid incorrect guesses | Easy uses the range 1–50 and allows 10 attempts | The game allowed 10 valid incorrect guesses before ending. Exact range boundaries still need a separate check | Pending |
| 10 | Medium difficulty and attempt limit | Selected Medium and entered a valid incorrect guess | Medium uses the range 1–100 and allows 8 attempts | After the first incorrect guess, the game displayed 7 attempts left. Exact range boundaries still need a separate check | Pending |
| 11 | Hard difficulty and attempt limit | Selected Hard and made valid incorrect guesses | Hard uses the range 1–500 and allows 10 attempts | The game allowed 10 valid incorrect guesses before ending and revealed the randomly selected secret number | Pending |
| 12 | Lowest and highest allowed guesses | Tested `1` and `50` in separate Easy rounds | Both boundary values are accepted as valid guesses | These exact boundary values have not yet been recorded in the test output | Pending |
| 13 | Running out of attempts | Set the secret to `42`, selected Easy, and entered 10 valid incorrect guesses | Game ends after 10 attempts and reveals the secret number | Game displayed "Game over!! Ran out of attempts" and revealed `42` | Yes |
| 14 | Time Challenge timeout | Set the time limit to 5 seconds, started Time Challenge, and waited before submitting a guess | Game reports timeout, ends the round, and reveals the secret number | Game displayed "Time up!! Game over!", revealed `42`, and reported that time had run out | Yes |
| 15 | Remaining time before a guess | Started Time Challenge with a 60-second limit and observed the timer before entering guesses | Remaining time is displayed before each guess | The game displayed "Time remaining (in seconds)" before the guess prompt, starting at approximately 60 seconds | Yes |
| 16 | Correct guess before timeout | Started Time Challenge with the secret set to `42` and entered `42` immediately | Game reports a win before time expires | Game displayed "Winner!!" and reported a win in 1 attempt | Yes |

### Test Results and Fixes

The initial testing identified a problem with the secret-number behavior: guesses were reported incorrectly during an earlier run. After checking the comparison logic and correcting the test setup, the deterministic Classic Mode test produced the expected results: `20` was too low, `50` was too high, and `42` won the game in 3 attempts.

Invalid inputs and out-of-range guesses were also tested. They were rejected without consuming attempts. The attempt-limit and timeout tests confirmed that the game ends and reveals the secret number when the player loses.

The remaining pending cases must be executed against the final version to verify the exact difficulty ranges and boundary values.

### Final Test Configuration

Before the final commit, restore the production settings:

- `DEBUG_SECRET = None` so the secret number is randomly generated.
- `TIME_LIMIT = 60` so Time Challenge uses the required 60-second limit.

After restoring these settings, rerun the main gameplay tests to confirm that the final configuration works as expected.
