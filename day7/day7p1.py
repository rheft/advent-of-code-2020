import re

QUESTION = '\033[94m'
ENDC = '\033[0m'

def sanitize_rule(rule: str) -> tuple:
    """Method for standardizing up the rule."""
    bag_key = rule.split(" bags contain ")[0]
    contained_bag = rule.split(" bags contain ")[1]
    contained_bag = re.sub("(\d)|(, )|(bag(s)?(.)?)", "", contained_bag)
    contained_bag_list = [re.sub("(^\s)|(\s$)", "", bag) for bag in contained_bag.split("  ") if bag not in [" ", "no other "]]
    contained_bag_set = set(contained_bag_list)
    return (bag_key, contained_bag_list)

def get_dependants(rules: list, key: str) -> set:
    """"""
    if len(rules[key]) == 0:
        return {key}
    
    else:
        full_set =  set()
        for i in rules[key]:
            full_set.update({i})
            full_set.update(get_dependants(rules, i))
        return full_set

def contains_target(rules: dict, target: str) -> int:
    """Determine the number of bags contaning the target."""
    return sum([1 if target in get_dependants(rules, key) else 0 for key in rules.keys()])

if __name__ == "__main__":
    rules = dict()
    shiny_bag_strings = []
    with open('day7/input.txt', 'r') as infile:
        for line in infile:
            value = line.replace('\n', '')
            sanitized_key, sanitized_set = sanitize_rule(value)
            rules[sanitized_key] = sanitized_set

    print(QUESTION+"How many bag colors can eventually contain at least one shiny gold bag?"+ENDC)
    print(contains_target(rules, "shiny gold"))
