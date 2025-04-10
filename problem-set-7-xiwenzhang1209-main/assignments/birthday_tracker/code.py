# TODO: your code here!
def organize(birthday_list):
  organized_birthdays = {}

  for birthday in birthday_list:
    month = birthday['month']
    day = birthday['day']
    name = birthday['name']

    if month not in organized_birthdays:
      organized_birthdays[month] = []
    organized_birthdays[month].append((day,name))
  
  for month in organized_birthdays:
    organized_birthdays[month].sort()
    organized_birthdays[month] = [name for _, name in organized_birthdays[month]]

  return organized_birthdays


## Test cases

def test_basic():
  bdays = [{
    "name": "Jenny",
    "month": 11,
    "day": 10
  }, {
    "name": "Forrest",
    "month": 11,
    "day": 20
  }, {
    "name": "Dan",
    "month": 5,
    "day": 6
  }, {
    "name": "Bubba",
    "month": 11,
    "day": 15
  }, {
    "name": "Cleveland",
    "month": 11,
    "day": 30
  }, {
    "name": "Dallas",
    "month": 1,
    "day": 12
  }, {
    "name": "Elvis",
    "month": 1,
    "day": 8
  }]
  result = organize(bdays)

  assert result == {
    1: ["Elvis", "Dallas"],
    5: ["Dan"],
    11: ["Jenny", "Bubba", "Forrest", "Cleveland"]
  }


def test_all_ones():
  bdays = [{
    "name": "Jenny",
    "month": 11,
    "day": 10
  }, {
    "name": "Forrest",
    "month": 10,
    "day": 20
  }, {
    "name": "Dan",
    "month": 5,
    "day": 6
  }, {
    "name": "Bubba",
    "month": 9,
    "day": 15
  }, {
    "name": "Cleveland",
    "month": 8,
    "day": 30
  }, {
    "name": "Dallas",
    "month": 7,
    "day": 12
  }, {
    "name": "Elvis",
    "month": 1,
    "day": 8
  }]
  result = organize(bdays)
  print(result)
  assert result == {
    11: ['Jenny'],
    10: ['Forrest'],
    5: ['Dan'],
    9: ['Bubba'],
    8: ['Cleveland'],
    7: ['Dallas'],
    1: ['Elvis']
  }


def test_empty():
  assert organize([]) == {}


def test_same_day():
  bdays = [
    {"name":"Alice","month": 3, "day":5},
    {"name":"Bob","month": 3, "day":5},
    {"name":"Charlie","month": 3, "day":5},
    {"name":"David","month": 3, "day":5}
  ]
  result = organize(bdays)
  print(result)
  assert result == {
    3:["Alice", "Bob", "Charlie", "David"]
  }