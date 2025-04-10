# TODO: your code here!

import csv

def load_file(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)
        for row in reader:
            if len(row) >= 2:
                date = row[0].strip()
                winning_numbers = row[1].strip()
                multplier = row[2].strip() if len(row) > 2 else None
                data.append([date, winning_numbers, multplier])
            else:
                print(f"Skipped row: {row}")
    return data

def find_winner(date, data):
    for row in data:
        if row[0] == date:
            return row[1]
    return None
    
def find_days_with_number(number, data):
    result = []
    for row in data:
        winning_numbers = row[1].split()
        if number in winning_numbers:
            result.append(row[0])
    return tuple(result)

def count_winning_numbers(data):
    counts = {}
    for row in data:
        winning_numbers = row[1].split()
        for number in winning_numbers:
            formatted_number = f"{int(number):02}"
            if formatted_number not in counts:
                counts[formatted_number] = 0
            counts[formatted_number] += 1
    return counts

def find_best_number(data):
    counts = count_winning_numbers(data)
    most_frequent_number = None
    max_count = 0

    for number in counts:
        current_count = counts[number]
        if current_count > max_count:
            max_count = current_count
            most_frequent_number = number
    if len(counts) == 0:
        return None
    return(most_frequent_number, max_count)

    


## Test cases

def test_load_file():
    data = load_file("assignments/lotto/numbers.csv")
    assert(len(data) == 1703)
    assert(data[0] == ["9/26/20", "11 21 27 36 62 24", "3"])
    assert(data[-1] == ["11/6/24", "12 17 37 58 62 04", "2"])

def test_find_winner_date_exists():
    data = load_file("assignments/lotto/numbers.csv")
    assert "09 11 17 19 55 01" == find_winner("8/16/23", data)

def test_find_winner_date_doesnt_exist():
    data = load_file("assignments/lotto/numbers.csv")
    assert None == find_winner("8/17/23", data)

def test_find_days_with_number_found():
    data = load_file("assignments/lotto/numbers.csv")
    result = sorted(find_days_with_number("60", data))
    assert 70 == len(result)
    assert "1/20/21" == result[0]
    assert "9/9/24" == result[-1]

def test_count_winning_numbers():
    data = load_file("assignments/lotto/numbers.csv")
    result = count_winning_numbers(data)
    assert 69 == len(result)

    assert 70 == result["60"]
    assert 186 == result["01"]
    assert 144 == result["30"]
    assert 98 == result["69"]

    # Assert that all numbers from 01 to 69 appear in the counts
    for x in range(69):
        assert f"{x+1:02}" in result

def test_find_best_number():
    data = load_file("assignments/lotto/numbers.csv")
    assert ("21", 207) == find_best_number(data)