# Importing Contacts

Skills for this problem: `Functional decomposition`, `Using pre-existing code`, `Debugging`,
`Functions - definition`, `References`, `Dictionaries - iteration`, `Nested data structures`,
`Sets`, `Data structures - choosing appropriately`, `File I/O`, `File I/O - JSON`

In this assignment, you will start with code for a Contacts application, similar to the application you wrote in PS8. To complete the problem, you will fix a bug in this code, and add the ability to load a set of contacts from a file.

# Requirements

1. There is a bug in the starter code keeping the `test_duplicate_number` test from passing. Find it
   and fix it.
1. Add a new option to the program: "6. Import contacts from file".
   * When a user selects this option, the program should load the file named
     `assignments/contacts_import/data.json`. This file should contains a JSON representation of
     the contact data.
   * The structure of the JSON in `data.json` does not match the structure of the data stored in the
      `contacts` variable in [main.py](main.py). You will need to transform the data to populate the
      `contacts` variable correctly.
      * Do **not** change the structure of the `contacts` variable to match the structure of the
        JSON - this will lead to much more work.
      * Create a full name by combining a first and last name, separated by a space.
   * When contacts are imported, they should not overwrite the existing contacts - their information
     should be added to the existing set of contacts!
      * e.g. If the contacts "Batman" and "Spongebob" were already added, and then "Dora" and
        "Peppa" are imported from the JSON file, the contact list should have all 4 contacts in it
        after the import.
      * If the contact "Batman" was already added, and the imported JSON has additional phone
        numbers for "Batman", then all of the prior phone numbers plus all of the phone numbers
        from the JSON should be listed after the import.

# Hints and grading notes

1. Importing contacts from a file involves an operation that is suspiciously similar to the
  "add a number" operation from the starter code. How can you re-use code for this in both places?
   * You must re-use code between "add a number" and importing contacts in order to get the
     `Functional decomposition` skill
2. To receive the `References` skill, no global variables should be used.
