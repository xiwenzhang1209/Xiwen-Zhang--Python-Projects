import random
from unittest import mock

def get_input():
  '''
  Get user input. This "wrapper" function exists to facilitate automated testing.
  '''
  return input()


def instructions():
  print("Welcome to the game!")
  print("You start with $10, and each roll costs $3.")
  print("If you roll a 1, your money is divided by 2")
  print("If you roll a 2, 3, or 4, you gain the amount you rolled")
  print("If you roll a 5, you gain 10")
  print("If you roll a 6, your money is doubled")
  print()
  print()


def take_single_turn(roll_num, money):
  '''
  Perform one roll.
  `num` is the number of rolls taken so far + 1
  `money` is the amount of money the player has after paying for this roll.
  returns: the amount of money the player has after the roll
  '''
  roll = random.randint(1, 6)

  print("Roll " + str(roll_num) + ": You rolled a " + str(roll))

  if roll == 1:
    print("Lose half!")
    money = money / 2
  elif roll == 5:
    print("Gain $10!")
    money = money + 10
  elif roll == 6:
    print("Double your money!")
    money = money * 2
  else:
    print("Gain " + str(roll) + "!")
    money = money + roll
  return roll, money


def take_turns(turns):
  '''
  Play a game for `turns` turns, or until the player runs out of money.
  returns: The amount of money the player has at the end of the game.
  '''
  total_money = 10
  rolls = 1
  original_turns = turns
  while total_money > 3 and turns > 0:
    print("You have $" + str(total_money) + ". " + str(turns) + " rolls left.")

    total_money = total_money - 3
    print("Taking $3 for the roll, leaving you with $" + str(total_money))
    total_money = take_single_turn(rolls, total_money)
    turns = turns - 1

  return total_money, original_turns - turns


def play_game():
  instructions()
  money = 10
  history = [(0, 10)]
  roll_num = 0

  while True:
    user_input = get_input("You have ${:.2f},what you want to do? ('r' to roll, 'h' to view history, 'q' to quit):")
    if user_input == 'q':
      print("You now ended with ${:.2f}")
      return history
    elif user_input == 'h':
      for roll, amount in history:
          print("Roll {roll}: ended turn with ${amount:.2f}")
    elif user_input == 'r':
      if money < 3:
        print("Not enough money to roll.")
        return history
      money -= 3
      roll_num += 1
      roll, money = take_single_turn(roll_num, money)
      history.append((roll,money))
    else:
        print("Invalid.")


if __name__ == '__main__':
  play_game()


## Test cases
# You are not required to add/modify test cases for this assignment.
# The test cases use "mocks", which we haven't covered in class.
# You can read more about mocking here: https://docs.python.org/3/library/unittest.mock-examples.html
# if you are interested.

def test_basic_game():
  random.seed(6)
  global get_input
  get_input = mock.MagicMock(name='get_input')
  # This is the input sent to your test
  get_input.side_effect = ['r', 'r', 'h', 'q']
  final_history = play_game()
  assert get_input.call_count == 4
  assert final_history == [(0, 10), (5, 17), (1, 7.0)]


def test_multiple_prints():
  random.seed(6)
  global get_input
  get_input = mock.MagicMock(name='get_input')
  # This is the input sent to your test
  get_input.side_effect = ['r', 'h', 'r', 'h', 'q']
  final_history = play_game()
  assert get_input.call_count == 5
  assert final_history == [(0, 10), (5, 17), (1, 7.0)]


def test_quit_immediately():
  random.seed(7)
  global get_input
  get_input = mock.MagicMock(name='get_input')
  # This is the input sent to your test
  get_input.side_effect = ['q']
  final_history = play_game()
  assert get_input.call_count == 1
  assert final_history == [(0, 10)]


def test_longer_game():
  random.seed(8)
  global get_input
  get_input = mock.MagicMock(name='get_input')
  # This is the input sent to your test
  get_input.side_effect = ['r', 'r', 'r', 'r', 'r', 'r', 'h', 'r', 'q']
  final_history = play_game()
  assert get_input.call_count == 9
  assert final_history == [(0, 10), (2, 9), (3, 9), (4, 10), (2, 9), (2, 8),
                           (6, 10), (1, 3.5)]