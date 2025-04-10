# Birthday tracker

Skills used in this problem: `Unit testing`, `Functions - definition`, `Functions - returning`,
`Cumulative algorithm`, `Lists - initialization, modification`, `Lists - iteration`,
`Dictionaries - initialization, modification`, `Dictionaries - iteration`, `Simple sorting`,
`Nested data structures`

Write a function to organize a list of birthdays: `organize(birthday_list)`. You'll be given a list
of birthdays, and will need to group the birthdays by month, and sort them by day of the month.

## Requirements


* Implement `organize(birthday_list)`
   * `birthday_list` is a list of dictionaries of the form:
     `{"name": <name>, "month": <month>, "day": <day>}`. `<month>` and `<day>` are integers.
   * `organize()` should return a dictionary where the keys are month numbers, and the values are
     lists of names. The list of names should be ordered by the birthday order within the month.
      * Hint: To sort a month by birthday order, create a list of tuples (day, name) for the monht,
        sort that, then create a new list in the same order with just the names.
* **Add at least one test case**

## Example

For this set of birthdays:
```
[
   { "name": "Jenny", "month": 11, "day": 10},
   { "name": "Forrest", "month": 11, "day": 20},
   { "name": "Dan", "month": 5, "day": 6},
   { "name": "Bubba", "month": 11, "day": 15},
   { "name": "Cleveland", "month": 11, "day": 30},
   { "name": "Dallas", "month": 1, "day": 12},
   { "name": "Elvis", "month": 1, "day": 8}
]
```

`organize(...)` should return:

```
{
   1: ["Elvis", "Dallas"],
   5: ["Dan"],
   11: ["Jenny", "Bubba", "Forrest", "Cleveland"]
}
```

Elvis and Dallas have birthdays in month 1. Elvis is on day 8, Dallas is on day 12, so Elvis appears
before Dallas in the list.

Only Dan has a birthday in month 5.

In month 11, Jenny, Bubba, Forrest, and Cleveland all have birthdays, and are in the order of their
actual birth days (10, 15, 20, 30).