from functools import reduce

QUESTION = '\033[94m'
ANSWER = '\033[93m'
ENDC = '\033[0m'

def get_next_location(dimensions: tuple, current_location: tuple, slope: tuple) -> tuple:
    """Calculates the next location in the array"""
    next_x = current_location[0]+slope[0]
    next_y = current_location[1]+slope[1]

    # Reset to the begining of the array because it repeats
    if next_x >= dimensions[0]:
        next_x = next_x % dimensions[0]

    # if we've reached the bottom return a -1 for next_y
    if next_y >= dimensions[1]:
        next_y = -1
    
    return (next_x, next_y)

def traverse_geography(geography: list, slope: tuple, starting_position: tuple = (0,0)) -> dict:
    """Determine the objects we see during our toboggan ride."""
    geography_dimensions = (len(geography[0]), len(geography))
    current_x, current_y = get_next_location(
        dimensions=geography_dimensions, 
        current_location=starting_position, 
        slope=slope
    )

    path = []
    while current_y != -1:
        path.append(geography[current_y][current_x])
        current_x, current_y = get_next_location(
            dimensions=geography_dimensions, 
            current_location=(current_x, current_y), 
            slope=slope
        )

    tree_count = sum([1 if obj == '#' else 0 for obj in path])
    return {"path": path, "tree_count": tree_count}

def multi_sloper(geography: list, slope_list: list) -> int:
    """Calculate the product of all the trees encountered in a list of slopes."""
    tree_counts = []
    for slope in slope_list:
        tree_counts.append(traverse_geography(geography=geography, slope=slope)['tree_count'])

    return reduce((lambda x, y: x * y), tree_counts)

if __name__ == "__main__":
    geography = []
    with open('day3/input.txt', 'r') as infile:
        for line in infile:
            value = list(line.replace('\n', ''))
            geography.append(value)

    problem_2_slope_list = [
        (1,1),
        (3,1),
        (5,1),
        (7,1),
        (1,2)
    ]

    traverse_result = traverse_geography(geography=geography, slope=(3,1))
    multi_sloper_result = multi_sloper(geography=geography, slope_list = problem_2_slope_list)

    print(QUESTION+"Problem A: \"How many trees we running into with a slope of 3,1?\""+ENDC)
    print(ANSWER+"Answer: "+str(traverse_result['tree_count'])+ENDC)
    print(QUESTION+"Problem B: \"Find the tree count for many slopes and find the product of those tree counts\""+ENDC)
    print(ANSWER+"Answer: "+str(multi_sloper_result)+ENDC)