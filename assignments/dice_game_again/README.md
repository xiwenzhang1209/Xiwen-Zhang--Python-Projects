# Dice Game... Again

Skills used in this problem: `Using pre-existing code`, `Variables`, `input()`,
`Functions - invocation`, `Functions - parameters`, `Functions - returning`, `Loops - while`,
`Lists - initialization, modification`, `Lists - iteration`, `Tuples`, `References`

This project contains code that runs our favorite dice game. This game was seen in PS2, PS3, and PS4.

## Rules

As a reminder, in this game:
* The player starts with $10.
* On each turn, a die is rolled, and the player accumulates money based on their roll.
  * If they roll a 1, their accumulated money is halved.
  * If they roll a 2, 3, or 4, they gain dollars equal to their roll.
  * If they roll a 5, they gain $10
  * If they roll a 6, their money is doubled.
* Each roll costs $3.

## Tasks overview

You start with the solution code from PS4. You'll be modifying this code to:
   * Allow an unlimited number of rolls
   * Save a history of rolls and money over the course of the game
   * Allow the user to print their roll history during the game.

## Task details
1. Modify the game to provide 3 options before each turn (including before the first roll):
   * `r` to roll again
   * `h` to print out the roll history
   * `q` to print out final money and stop the game
2. Change `play_game()` to return the game history when the game finishes.
   * The returned game history should be a list that represents the roll history from the game, ordered from oldest roll (index: 0) to newest roll (index: -1).
   * Each item in the returned history should be a 2-tuple containing 2 integers: `roll` and `money`, where `roll` is the number rolled that turn, and `money` is the amount of money the player has at the end of the turn (**after** paying for the roll and modifying money based on the roll).
   * The history **cannot** be held in a global variable, and you must use at least one helper function which modifies the history. You will not receive the "references" skill if you don't follow this requirement.
   * See the test cases for examples of the expected return values.
3. Between each turn, your program should print:
   * What the player just rolled.
   * How much money they gained/lost on that turn.
   * The amount of money the player has after the turn.
4. When printing the history, your program should print:
   * That the player started with $10
   * The roll value and ending money for each turn
   * **There are no automated tests for the printing**, but these will be reviewed during grading.

**Important notes**:

1. You are welcome to modify or re-write the starter code as much as necessary.

2. The automated tests for this problem target `play_game()`. In order to get them to pass:
   * You must have a function called `play_game()` that takes no arguments and returns the game history.
   * You must use the `get_input()` function to get user input, rather than using `input()` directly.
   * The roll history should always start with a tuple `(0, 10)` at the beginning of the game.
   * The game should ask for input before the first turn (i.e. after printing instructions, the user
     should be prompted to enter r/h/q even before the first roll).

3. The game's history must not be held in a global variable (as noted above).

## Hints

* You can use the history list to hold all of the game state. It contains all the information you
  need to keep track of (the roll count, the rolls, and the amount of money at the end of each turn).
* If you create your history list in `play_game()`, then pass it into the helper functions that need
  to either use it or modify it, then you shouldn't have to pass much (or any) other data around in
  your program.


## Sample output

Here is some sample output from a game. For this assignment, your output does **not** have to match
this exactly, but it must follow the guidelines above.
```
Welcome to the game!
You start with $10, and each roll costs $3.
If you roll a 1, your money is divided by 2
If you roll a 2, 3, or 4, you gain the amount you rolled
If you roll a 5, you gain 10
If you roll a 6, your money is doubled


You have $10, what would you like to do?
'r' to roll again, 'h' to print history, 'q' to quit:
r
Taking $3 for the roll, leaving you with $7
Roll 1: You rolled a 6
Double your money!
You have $14, what would you like to do?
'r' to roll again, 'h' to print history, 'q' to quit:
r
Taking $3 for the roll, leaving you with $11
Roll 2: You rolled a 4
Gain 4!
You have $15, what would you like to do?
'r' to roll again, 'h' to print history, 'q' to quit:
h
Started the game with $10
Rolled a 6, ended turn with $14
Rolled a 4, ended turn with $15
You have $15, what would you like to do?
'r' to roll again, 'h' to print history, 'q' to quit:
r
Taking $3 for the roll, leaving you with $12
Roll 3: You rolled a 4
Gain 4!
You have $16, what would you like to do?
'r' to roll again, 'h' to print history, 'q' to quit:
h
Started the game with $10
Rolled a 6, ended turn with $14
Rolled a 4, ended turn with $15
Rolled a 4, ended turn with $16
You have $16, what would you like to do?
'r' to roll again, 'h' to print history, 'q' to quit:
q
Good game, you ended with $16
```