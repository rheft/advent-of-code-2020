import re

QUESTION = '\033[94m'
ENDC = '\033[0m'

def parse_input(instruction: str) -> tuple:
    action = instruction[0]
    magnitude = int(instruction[1:])

    return (action, magnitude)

def p1_manhattan_distance(directions: list) -> int:
    current_direction = 0
    compass = {
        0: "E",
        90: "N",
        180: "W",
        270: "S"
    }
    distances = {
        "N": 0, 
        "E": 0,
        "S": 0,
        "W": 0
    }
    
    for instruction in directions:
        action, magnitude = instruction[0], instruction[1]
        if action in distances.keys():
            distances[action] += magnitude
        elif action == "F":
            distances[compass[current_direction%360]] += magnitude
        elif action == "R":
            current_direction -= magnitude
        elif action == "L":
            current_direction += magnitude

    manhattan_distance = abs(distances["N"]-distances["S"])+abs(distances["E"]-distances["W"])
    return manhattan_distance

def update_waypoint(current_direction: int, relative_waypoint_location: list, next_change: int) -> list:
    compass = {
        0: relative_waypoint_location,
        90: [-relative_waypoint_location[1], relative_waypoint_location[0]],
        180: [-relative_waypoint_location[0], -relative_waypoint_location[1]],
        270: [relative_waypoint_location[1], -relative_waypoint_location[0]],
        360: relative_waypoint_location
    }

    return compass[next_change] if next_change >= 0 else compass[360+next_change]

def p2_manhattan_distance(directions: list) -> int:
    relative_waypoint_location = [10, 1]
    ship_location = [0,0]
    current_direction = 0
    
    for instruction in directions:
        action, magnitude = instruction[0], instruction[1]
        if action == "N":
            relative_waypoint_location[1] += magnitude
        if action == "S":
            relative_waypoint_location[1] -= magnitude
        if action == "E":
            relative_waypoint_location[0] += magnitude
        if action == "W":
            relative_waypoint_location[0] -= magnitude
        if action == "F":
            ship_location[0] += magnitude*relative_waypoint_location[0]
            ship_location[1] += magnitude*relative_waypoint_location[1]
        if action == "R":
            current_direction -= magnitude
            relative_waypoint_location = update_waypoint(current_direction, relative_waypoint_location, -magnitude)
        if action == "L":
            current_direction += magnitude
            relative_waypoint_location = update_waypoint(current_direction, relative_waypoint_location, magnitude)

    return abs(ship_location[0])+abs(ship_location[1])

if __name__ == "__main__":
    directions = []
    directory = re.sub("\/.*", "", __file__)
    with open(f'{directory}/input.txt', 'r') as infile:
        for line in infile:
            value = line.replace('\n', '')
            input_value = parse_input(value)
            directions.append(input_value)

    p1_manhattan_dist = p1_manhattan_distance(directions)
    p2_manhattan_dist = p2_manhattan_distance(directions)

    print(QUESTION+"Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?"+ENDC)
    print(p1_manhattan_dist)

    print(QUESTION+"Figure out where the navigation instructions actually lead. What is the Manhattan distance between that location and the ship's starting position?"+ENDC)
    print(p2_manhattan_dist)
