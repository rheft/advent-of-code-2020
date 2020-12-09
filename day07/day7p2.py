import re

QUESTION = '\033[94m'
ENDC = '\033[0m'

def sanitize_rule(rule: str) -> tuple:
    """Method for standardizing up the rule."""
    bag_key = rule.split(" bags contain ")[0]
    contained_bag = rule.split(" bags contain ")[1]
    contained_bag = re.sub("( bag(s)?(\.)?)", "", contained_bag)
    contained_bag = contained_bag.split(", ")
    
    if "no other" in contained_bag:
        return (bag_key, [])

    rule_values = [(int(value[0]), value[2:]) for value in contained_bag]
    return (bag_key, rule_values)

def get_dependants(rules: list, key: str) -> set:
    """"""
    if len(rules[key]) == 0:
        return 0
    
    else:
        sub_amount = 0
        for i in rules[key]:
            required_num = i[0]
            sub_amount += required_num+(required_num*get_dependants(rules, i[1]))
        return sub_amount

if __name__ == "__main__":
    rules = dict()
    with open('day7/input.txt', 'r') as infile:
        for line in infile:
            sanitized_key, bag_rule = sanitize_rule(line.replace('\n', ''))
            rules[sanitized_key] = bag_rule
    
    print(QUESTION+"How many individual bags are required inside your single shiny gold bag?"+ENDC)
    print(get_dependants(rules, "shiny gold"))
