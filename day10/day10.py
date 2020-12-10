import re
from itertools import combinations
from functools import reduce

QUESTION = '\033[94m'
ENDC = '\033[0m'

def count_valid_combinations(adapters: list) -> int:
    """Count the number of valid combination of adapters"""
    required = {0}
    not_required = []
    current_not_required_subgroup = []

    for index, value in enumerate(adapters):
        last = index == len(adapters)-1
        if last:
            diff = 3
        else:
            diff = adapters[index+1]-value
        
        # A difference of 3 between two numbers indicates both are required to form a valid adaptation
        if diff == 3:
            required.add(adapters[index])
            if not last:
                required.add(adapters[index+1])
        
        # Otherwise the number is not necessary in EVERY combination
        # Also group the unnecessary values together for later ie [[1,2,3], [8,9], ...]
        elif value not in required:
            if len(current_not_required_subgroup) == 0 or value == current_not_required_subgroup[-1]+1:
                current_not_required_subgroup.append(value)
            else:
                not_required.append(current_not_required_subgroup)
                current_not_required_subgroup = [value]
    
    # Add the last subgroup into the overall list because im lazy
    not_required.append(current_not_required_subgroup)

    # because we we cant have >3 values seperation we need the combinations of the maximum of (0 or length of subgroup - 2) 
    # ie if your subgroup values are [1,2,3] removing all of them would lead to an invalid combination so you need to at minimum pick 1
    # get the combinations of each subgroup
    not_required_combinations = []
    for subgroup in not_required:
        combination_counts = []
        for i in range(max(len(subgroup)-2, 0), len(subgroup)+1):
            combination_counts.append(len(list(combinations(subgroup, i))))
        not_required_combinations.append(sum(combination_counts))

    # once youve found all of the possible combination for each subgroup, get the product of the list
    total_combination_counts = reduce(lambda x, y: x*y, not_required_combinations)
    return total_combination_counts

def adaptations(adapters: list) -> dict:
    """Determine the number of adaptations we need to make for each difference (1, 2 or 3)."""
    adaptations = {1:0, 2:0, 3:0}
    for index, value in enumerate(adapters):
        if index == len(adapters)-1:
            diff = 3
        else:
            diff = adapters[index+1]-value
        adaptations[diff] += 1

    return adaptations  

if __name__ == "__main__":
    adapters = [0]
    directory = re.sub("\/.*", "", __file__)
    with open(f'{directory}/input.txt', 'r') as infile:
        for line in infile:
            value = int(line.replace('\n', ''))
            adapters.append(value)

    adapters.sort()
    valid_count = count_valid_combinations(adapters)
    adaptation_counts = adaptations(adapters)

    print(QUESTION+"What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?"+ENDC)
    print(adaptation_counts[1]*adaptation_counts[3])

    print(QUESTION+"What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?"+ENDC)
    print(valid_count)