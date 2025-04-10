import math
from os import name

## TODO: Add your class here

class TrailInfo:
    def __init__(self, name, difficulty):
        self.name = name 
        if difficulty < 1 or difficulty > 5:
            self.difficulty = 3
        else:
            self.difficulty = difficulty
        self.waypoints = []

    def add_waypoint(self, x, y):
        self.waypoints.append((x, y))
        return self.waypoints 
    
    def get_length(self):
        total_length = 0
        for i in range(1, len(self.waypoints)):
            x1, y1 = self.waypoints[i-1]
            x2, y2 = self.waypoints[i]
            distance = math.sqrt((x2 - x1)**2 + (y2 -y1)**2)
            total_length += distance
        return total_length
    
    def get_estimated_hike_time(self):
        return self.get_length() * self.difficulty
    
    def get_route(self):
        route_string = ""
        for i, waypoint in enumerate(self.waypoints):
            if i > 0:
                route_string += " -> "
            route_string += f"({waypoint[0]}, {waypoint[1]})"
        return route_string




## TODO: Add your test cases here
def test_add_waypoint():
    t = TrailInfo("test", 4)
    t.add_waypoint(0, 0)
    t.add_waypoint(1, 1)
    assert t.waypoints == [(0, 0), (1, 1)]

def test_get_length_no_points():
    t = TrailInfo("test", 4)
    assert t.get_length() == 0.0

def test_get_estimated_hike_time_no_points():
    t = TrailInfo("test", 4)
    assert t.get_estimated_hike_time() == 0.0

def test_get_route_no_points():
    t = TrailInfo("test", 4)
    assert t.get_route() == ""



## Provided test cases, don't edit





def test_create():
    t = TrailInfo("Shortie", 1)
    assert t.name == "Shortie"
    assert t.difficulty == 1

def test_create_out_of_bounds():
    t = TrailInfo("K2", 10)
    assert t.name == "K2"
    assert t.difficulty == 3

def test_get_length():
    t = TrailInfo("test", 4)
    t.add_waypoint(0, 0)
    t.add_waypoint(0, 1)
    t.add_waypoint(0, 2)
    t.add_waypoint(1, 2)
    t.add_waypoint(2, 2)
    assert t.get_length() == 4.0

def test_get_length_one_point():
    t = TrailInfo("test", 4)
    t.add_waypoint(0, 0)
    assert t.get_length() == 0.0

def test_get_length_float():
    t = TrailInfo("test", 5)
    t.add_waypoint(0, 0)
    t.add_waypoint(5, 10)
    t.add_waypoint(7, 16)
    t.add_waypoint(1, 8)
    assert math.isclose(t.get_length(), 27.5048952078)

def test_get_estimated_time():
    t = TrailInfo("test", 2)
    t.add_waypoint(0, 0)
    t.add_waypoint(0, 1)
    t.add_waypoint(0, 2)
    t.add_waypoint(1, 2)
    t.add_waypoint(2, 2)
    assert t.get_estimated_hike_time() == 8.0

def test_get_estimated_time_float():
    t = TrailInfo("test", 5)
    t.add_waypoint(0, 0)
    t.add_waypoint(5, 10)
    t.add_waypoint(7, 16)
    t.add_waypoint(1, 8)
    assert math.isclose(t.get_estimated_hike_time(), 137.52447603917)

def test_get_route():
    t = TrailInfo("test", 4)
    t.add_waypoint(0, 0)
    t.add_waypoint(0, 1)
    t.add_waypoint(0, 2)
    t.add_waypoint(1, 2)
    t.add_waypoint(2, 2)
    assert t.get_route() == "(0, 0) -> (0, 1) -> (0, 2) -> (1, 2) -> (2, 2)"

def test_get_route_one_point():
    t = TrailInfo("test", 4)
    t.add_waypoint(0, 1)
    assert t.get_route() == "(0, 1)"