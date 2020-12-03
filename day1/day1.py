QUESTION = '\033[94m'
ANSWER = '\033[93m'
ENDC = '\033[0m'

def expense_report_2(report: set) -> int:
    """AoC day 1.a:
        1. find the 2 values in a list that sum to 2020
        2. return those two numbers multiplied together
        
        Im an idiot, conditional 'in' executes another loop so this wasn't actually very efficient...
        converting to a set object improves performance by a lot
    """
    for value in report:
        diff = 2020-value # value cant be larger than 2020 and pass
        if diff in report:
            return value*diff

def expense_report_3(report: set) -> int:
    """AoC day 1.b:
        1. find the 3 values in a list that sum to 2020
        2. return those three numbers multiplied together

        Im an idiot, conditional 'in' executes another loop so this wasn't actually very efficient...
        converting to a set object improves performance by a lot
    """
    for x_value in report:
        for y_value in report:
            if y_value <= x_value:
                continue # Sets are inherintly sorted in python so if y is smaller or equal to x we've already checked it
            diff = 2020-(x_value+y_value) # value cant be larger than 2020 and pass
            if diff in report:
                return x_value*y_value*diff

if __name__ == "__main__":
    expense_list = []
    with open('day1/input.txt', 'r') as infile:
        for line in infile:
            value = int(line.replace('\n', ''))
            expense_list.append(value)

    # Im an idiot, conditional 'in' executes another loop so this wasn't actually very efficient...
    # converting to a set object improves performance by a lot
    expense_report_set = set(expense_list)
    
    report_2 = expense_report_2(expense_report_set)
    report_3 = expense_report_3(expense_report_set)
    print(QUESTION+"Problem A: \"find the two entries that sum to 2020\""+ENDC)
    print(ANSWER+"Answer: "+str(report_2)+ENDC)
    print(QUESTION+"Problem B: \"what is the product of the three entries that sum to 2020\""+ENDC)
    print(ANSWER+"Answer:"+str(report_3)+ENDC)