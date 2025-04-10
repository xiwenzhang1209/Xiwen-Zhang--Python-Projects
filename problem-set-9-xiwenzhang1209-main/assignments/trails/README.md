# Trail tracker

Skills for this problem: `Unit testing`, `Expressions`, `Functions - parameters`,
`Fencepost algorithm`, `Lists - initialization, modification`, `Lists - iteration`,
`Lists - nested lists`, `Tuples`, `Nested data structures`,
`Data structures - choosing appropriately`, `Classes - definition`, `Classes - usage`

In this problem, you will write a class to track different information about hiking trails in
[code.py](code.py).

Trails have:
* A name
* An ordered collection of waypoints that make up the route. Each waypoint has x and y coordinates.
* A difficulty rating
* A length, which is the sum of the distances between each waypoint.
* An "estimated hike time" based on the total trail distance and difficulty.

## Requirements

1. Write a class named `TrailInfo`. It should have the following methods:

* A constructor (`__init__`) which takes in the name of the trail (`str`) and difficulty
  (`int` between 1 and 5) as arguments.
   * A new `TrailInfo` starts with no waypoints.
   * If a value < 1 or > 5 is passed in for difficulty, the difficulty should be set to 3.
* `add_waypoint(x, y)` - This method adds a waypoint to the trail
* `get_length()` - This method computes the total length of the trail
   * The distance between two points can be computed with the Pythagorean theorem: `sqrt(a^2 + b^2)`
   * For two coordinates, `(x1, y1)` and `(x2, y2)` this would be: `sqrt((x1-x2)^2, (y1-y2)^2)`
* `get_estimated_hike_time()` - This method computes the estimated hike time
   * The estimated hike time is computed by the formula: `total length * difficulty`
* `get_route()` - This method creates and returns a string describing the route.
   * The format of each way point should be `(x, y)`
   * The sequence of waypoints should be printed out with `->` in between each one.
   * e.g. a TrailInfo with way points `(0, 0)`, `(1, 2)`, `(4, 5)` would produce `(0, 0) -> (1, 2) -> (4, 5)` for the route string.

2. Add one test case for each method above. Some test cases are provided, you can use them as
   starting points for your own cases.