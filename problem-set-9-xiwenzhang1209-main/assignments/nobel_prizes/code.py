## TODO: your code here!


## Provided test cases, do not edit

import json
def load_nobels(filename="assignments/nobel_prizes/nobels.json"):
    with open(filename, 'r') as f:
        return json.load(f)
    
def count_prizes():
    data = load_nobels()
    return len(data['prizes'])

def count_winners():
    data = load_nobels()
    count = 0
    for prize in data['prizes']:
        if 'laureates' in prize:
            count += len(prize['laureates'])
    return count

def list_categories():
    data = load_nobels()
    categories = set()
    for prize in data['prizes']:
        if 'category' in prize:
            categories.add(prize['category'].lower())
    return sorted(list(categories))

def counts_by_category():
    data = load_nobels()
    categories = {}
    for prize in data['prizes']:
        if 'category' in prize:
            category = prize['category'].lower()
            if category in categories:
                categories[category] +=1
            else:
                categories[category] =1
    return categories

def repeat_winners():
    data = load_nobels()
    winners = {}
    for prize in data['prizes']:
        if 'laureates' in prize:
            for laureate in prize['laureates']:
                if 'firstname' in laureate and 'surname' in laureate:
                    name = f"{laureate['firstname']} {laureate['surname']}"
                elif 'firstname' in laureate:
                    name = laureate['firstname']
                elif 'name' in laureate:
                    name = laureate['name']
                else:
                    continue
                if name in winners:
                    winners[name] += 1
                else:
                    winners[name] = 1
    return sorted([name for name, count in winners.items() if count > 1])


def test_count_prizes():
    assert count_prizes() == 670

def test_count_winners():
    assert count_winners() == 1000

def test_list_categores():
    assert list_categories() == ['chemistry', 'economics', 'literature', 'medicine', 'peace', 'physics']

def test_counts_by_category():
    assert counts_by_category() == {
        'chemistry': 123,
        'economics': 55,
        'literature': 123,
        'medicine': 123,
        'peace': 123,
        'physics': 123,
    }

def test_repeat_winners():
    assert repeat_winners() == [
        'Barry Sharpless',
        'Frederick Sanger',
        'International Committee of the Red Cross',
        'John Bardeen',
        'Linus Pauling',
        'Marie Curie',
        'Office of the United Nations High Commissioner for Refugees',
    ]