# TODO: Your code here!
def filter_ages(data, min, max):
  return[name for name, age in data.items() if min<=age<=max]

## Tests

def test_basic():
  assert sorted(
    filter_ages({
      "Abe": 10,
      "Molly": 15,
      "Sarah": 20,
      "Rohan": 11
    }, 12, 20)) == sorted(["Molly", "Sarah"])


def test_empty():
  assert filter_ages({}, 10, 20) == []


def test_empty_result():
  assert sorted(
    filter_ages({
      "Abe": 10,
      "Molly": 15,
      "Sarah": 20,
      "Rohan": 12
    }, 30, 40)) == sorted([])


def test_bounds():
  assert sorted(
    filter_ages({
      "Abe": 10,
      "Molly": 15,
      "Sarah": 20,
      "Rohan": 11
    }, 10, 15)) == sorted(["Abe", "Molly", "Rohan"])

def test_overlap():
  assert sorted(
    filter_ages({
      "Abe": 25,
      "Molly": 18,
      "Sarah": 30,
      "Rohan": 18,
      "Evan": 25
    },18, 25)) == sorted(["Abe","Molly","Rohan","Evan"])

def test_only():
  assert sorted(
    filter_ages({
      "Abe": 25,
      "Molly": 18,
      "Sarah": 30,
      "Rohan": 18,
      "Evan": 25
    }, 30, 30)) == sorted(["Sarah"])
  