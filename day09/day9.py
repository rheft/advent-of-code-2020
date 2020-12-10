import re

QUESTION = '\033[94m'
ENDC = '\033[0m'

def value_meets_criteria(previous_values: set, target_value: int) -> bool:
    """Determine if the next value in the list meets the expected criteria."""
    for value in previous_values:
        if target_value-value in previous_values:
            return True

    return False

def find_invalid_number(value_list: list, max_range: int) -> int:
    """Given a list of values and a range to cover, determine if the next value in the list is valid defined by the criteria function."""
    previous_values = []
    for value in value_list:
        if len(previous_values) >= max_range:
            if value_meets_criteria(set(previous_values), value):
                del previous_values[0]
            else:
                break
        
        previous_values.append(value)

    return value

def find_encryption_weakness(value_list: list, target_value:int) -> int:
    """Given a list of values find the contiguous values that sum to the target_value and return the sum of the max and min of thos values."""
    starting_position = 0
    while starting_position <= len(value_list):
        diff = target_value
        contiguous_set = []
        
        for value in value_list[starting_position:]:
            contiguous_set.append(value)
            diff = diff-value
            if diff == 0:
                return max(contiguous_set)+min(contiguous_set)
        
        starting_position += 1

if __name__ == "__main__":
    MAX_RANGE = 25

    value_list = []
    directory = re.sub("\/.*", "", __file__)
    with open(f'{directory}/input.txt', 'r') as infile:
        for line in infile:
            value = int(line.replace('\n', ''))
            value_list.append(value)

    invalid_number = find_invalid_number(value_list, MAX_RANGE)
    encryption_weakness = find_encryption_weakness(value_list, invalid_number)

    print(QUESTION+"The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it. What is the first number that does not have this property?"+ENDC)
    print(invalid_number)

    print(QUESTION+"What is the encryption weakness in your XMAS-encrypted list of numbers?"+ENDC)
    print(encryption_weakness)