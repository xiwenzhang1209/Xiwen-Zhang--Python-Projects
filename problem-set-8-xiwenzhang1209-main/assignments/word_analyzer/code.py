## TODO: your code here!

def analyze_file(filename):
    total_words = 0
    unique_words = set()

    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            total_words += len(words)
            unique_words.update(words)

    return (total_words, len(unique_words))



def test_analyze():
    assert analyze_file('assignments/word_analyzer/dracula.txt') == (160284, 18158)