# Analyzing Nobel Prizes

Skills for this assignment: `Functional decomposition`, `Debugging`, `Conditionals - if/elif/else`,
`Conditionals - logic`, `Functions - definition`, `Functions - returning`, `Loops - for/range`,
`Cumulative algorithm`, `Loops - nested for/range`, `Lists - iteration`,
`Dictionaries - initialization, modification`, `Dictionaries - iteration`,
`Dictionaries - filtering`, `Simple sorting`, `Nested data structures`, `Sets`, `File I/O`,
`File I/O - JSON`

In this assignment, you will write code in [code.py](code.py) that answers questions about the data in
[nobels.json](nobels.json).

# Requirements

1. Write a function `count_prizes()` which counts the number of prizes represented in the file.
   * Note that a single prize may be shared among multiple laureates (winners). For this function, you should count the number of prizes, not the number of people who won prizes.
1. Write a function `count_winners()` which counts the total number of laureates (winners) in the file.
1. Write a function `list_categories()` which returns a **list, sorted alphabetically** of all the categories in which prizes were awarded. The list should not contain duplicates.
1. Write a function `counts_by_category()` which returns a dictionary which contains the count of prizes awarded per category.
1. Write a function `repeat_winners()` which returns a **list, sorted alphabetically** containing the full names of every winner who has won multiple prizes.
   * A "full name" here is formatted as `<firstname> <surname>`, or, if no surname exists, just `<firstname>`

# Hints and grading notes
1. The path to the file is `assignments/nobel_prizes/nobels.json`.
1. `nobels.json` contains real data, and real data tends to be "dirty" - it doesn't always follow to the rules! Some entries will be missing expected fields.
   * When you first write your functions and run the tests, you will get errors. You'll need to debug in order to figure out where the problems are in the file, and then add checks to your code to handle those cases.
   * Do **not** edit the json file itself to "fix" the errors. If you do, you will lose credit for `Debugging`, as well as other skills.
1. Each function needs to load the file. You should not copy/paste all the code needed to load the file into each function. In order to get credit for the `Functional decomposition` skill, you must not repeat the file loading code, or use any global variables.