import re
from pprint import pprint

QUESTION = '\033[94m'
ENDC = '\033[0m'

def determine_line_of_sight(seats: list, target_seat: tuple, problem: str) -> list:
    target_y, target_x = target_seat[0], target_seat[1]
    los_positions = []

    y_step = x_step = 0
    for trajectory in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
        y = target_y+trajectory[0]
        x = target_x+trajectory[1]
        los = None
        while y >= 0 and y <= len(seats)-1 and x >= 0 and x <= len(seats[0])-1:
            if seats[y][x] != '.':
                los = (y,x)
                break
            if problem == 'p1':
                break # Breaks on first pass
            y+=trajectory[0]
            x+=trajectory[1]
        los_positions.append(los)
    
    return los_positions

def check_seat_changes(seating_chart: list, current_position: str, target_los_positions:list, problem: str) -> bool:
    count_occupied_seats = 0
    for value in target_los_positions:
        if value is None:
            continue
        if seating_chart[value[0]][value[1]] == "#":
            count_occupied_seats += 1

    if current_position == "L":
        return count_occupied_seats == 0
    else:
        seat_threshold = 4 if problem == 'p1' else 5
        return count_occupied_seats >= seat_threshold

def update_seating_chart(seating_chart: list, los_positions: dict, problem: str) -> list:
    updated_seating_chart = []
    for y_index, y_value in enumerate(seating_chart):
        updated_y_chart = []
        for x_index, x_value in enumerate(y_value):
            if x_value == ".":
                updated_y_chart.append(x_value)
                continue
            updated_value = x_value
            seat_will_change = check_seat_changes(seating_chart, x_value, los_positions[(y_index),(x_index)], problem)
            if seat_will_change:
                updated_value = "#" if x_value == "L" else "L"

            updated_y_chart.append(updated_value)
        updated_seating_chart.append(updated_y_chart)

    return (updated_seating_chart, updated_seating_chart!=seating_chart)

if __name__ == "__main__":
    seating_chart_p1 = []
    directory = re.sub("\/.*", "", __file__)
    with open(f'{directory}/input.txt', 'r') as infile:
        for line in infile:
            value = list(line.replace('\n', ''))
            seating_chart_p1.append(value)
    
    seating_chart_p2 = seating_chart_p1.copy()

    los_positions_p1 = {(y_index, x_index): determine_line_of_sight(seating_chart_p1, (y_index, x_index), 'p1') for y_index, y in enumerate(seating_chart_p1) for x_index, x in enumerate(y)}
    los_positions_p2 = {(y_index, x_index): determine_line_of_sight(seating_chart_p2, (y_index, x_index), 'p2') for y_index, y in enumerate(seating_chart_p2) for x_index, x in enumerate(y)}
    
    state_changed_1 = True
    while state_changed_1:
        seating_chart_p1, state_changed_1 = update_seating_chart(seating_chart_p1, los_positions_p1, 'p1')

    state_changed_2 = True
    while state_changed_2:
        seating_chart_p2, state_changed_2 = update_seating_chart(seating_chart_p2, los_positions_p2, 'p2')
    
    count_occupied_seats_p1 = sum([1 if x == '#' else 0 for y in seating_chart_p1 for x in y])
    print(QUESTION+"Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?"+ENDC)
    print(count_occupied_seats_p1)

    count_occupied_seats_p2 = sum([1 if x == '#' else 0 for y in seating_chart_p2 for x in y])
    print(QUESTION+"Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?"+ENDC)
    print(count_occupied_seats_p2)