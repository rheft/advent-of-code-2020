from pprint import pprint
from functools import reduce
import re
import time

QUESTION = '\033[94m'
ENDC = '\033[0m'

def determine_minimum_depature_time(arrival_time: int, bus_times: list) -> int:
    """"""
    bus_times = [int(bus_time) for bus_time in bus_times if bus_time != 'x']
    diffs = [int(bus_time)-(arrival_time%int(bus_time)) for bus_time in bus_times if bus_time != 'x']
    smallest_diff = min(diffs)
    return smallest_diff, bus_times[diffs.index(smallest_diff)]

def determine_bus_departure_train(bus_ids: list) -> int:
    """Determine at what time we create a train of bus departures."""
    mods = {int(bus): -i % int(bus) for i, bus in enumerate(bus_ids) if bus != "x"}
    vals = list(reversed(sorted(mods)))
    val = mods[vals[0]]
    r = vals[0]
    # creds: https://github.com/q-viper/Adevent-Of-Code-2020/blob/master/Advent%20of%20code.ipynb read/open at your own risk 😂
    # need to better understand whats happenin here, waited 30+hrs before stealing a solution.
    for b in vals[1:]:
        while val % b != mods[b]:
            val += r
        r *= b
        
    return val

if __name__ == "__main__":
    input_data = []
    directory = re.sub("\/.*", "", __file__)
    with open(f'{directory}/input.txt', 'r') as infile:
        for line in infile:
            value = line.replace('\n', '')
            input_data.append(value)
    
    arrival_time = int(input_data[0])
    bus_times = input_data[1].split(',')
    
    min_depature_time, bus = determine_minimum_depature_time(arrival_time, bus_times)
    print(QUESTION+"What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?"+ENDC)
    print(min_depature_time*bus)

    earliest_t = determine_bus_departure_train(bus_times)

    print(QUESTION+"What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?"+ENDC)
    print(earliest_t)
    
