import math
    
QUESTION = '\033[94m'
ANSWER = '\033[93m'
ENDC = '\033[0m'

def get_seat_id(boarding_pass: str) -> int:
    """Determine seat id value for a boarding pass."""
    row_value = 0
    col_value = 0

    max_row_value = 127
    min_row_value = 0

    max_col_value = 7
    min_col_value = 0

    # determine the the row value
    for letter in boarding_pass[:7]:
        if letter == "F":
            max_row_value = math.floor((max_row_value+min_row_value)/2)
        elif letter == "B":
            min_row_value = math.ceil((max_row_value+min_row_value)/2)
        
        if min_row_value==max_row_value:
            row_value = min_row_value
            break

    # determine the column value
    for letter in boarding_pass[7:]:
        if letter == "R":
            min_col_value = math.ceil((max_col_value+min_col_value)/2)
        elif letter == "L":
            max_col_value = math.floor((max_col_value+min_col_value)/2)

        if min_col_value==max_col_value:
            col_value = min_col_value
            break

    return (row_value*8)+col_value


if __name__ == "__main__":
    boarding_passes_ids = []
    with open('day5/input.txt', 'r') as infile:
        for line in infile:
            value = line.replace('\n', '')
            boarding_passes_ids.append(get_seat_id(value))
    
    print(QUESTION+"Question1: find the max seat id for each seat on the plane."+ENDC)
    print(max(boarding_passes_ids))

    boarding_passes_ids.sort()
    offset = boarding_passes_ids[0] # offset would be our min value
    for value in boarding_passes_ids:
        # we only need the first incorrection
        if value != offset:
            break
        offset += 1
    
    print(QUESTION+"Question2: What seat is yours?"+ENDC)
    print(offset)