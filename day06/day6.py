QUESTION = '\033[94m'
ENDC = '\033[0m'

def unique_answers(answer_string: str) -> int:
    """Return the length of the unique letters"""
    return len(set(answer_string.replace(" ", "")))

def all_answered(answer_string: str) -> int:
    """Return count of answers that everyone agreed on."""
    num_groups = len(answer_string.split(" ")) - 1 # remove leading space
    letter_counts = dict()
    count_letter_in_all = 0

    for group in answer_string.split(" "):
        if group == "":
            continue
        for letter in set(group):
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
            if letter_counts[letter] == num_groups:
                count_letter_in_all += 1
    
    return count_letter_in_all

if __name__ == "__main__":
    answer_lengths = []
    letter_in_all_counts = []
    current_group = ''
    with open('day6/input.txt', 'r') as infile:
        for line in infile:
            value = line.replace('\n', '')
            if value == '':
                answer_lengths.append(unique_answers(current_group))
                letter_in_all_counts.append(all_answered(current_group))
                current_group = ''
            else:
                current_group += f" {value}"
        # Get the last one
        answer_lengths.append(unique_answers(current_group))
        letter_in_all_counts.append(all_answered(current_group))

    print(QUESTION+"For each group, count the number of questions to which anyone answered \"yes\""+ENDC)
    print(sum(answer_lengths))
    print(QUESTION+"For each group, count the number of questions to which everyone answered \"yes\""+ENDC)
    print(sum(letter_in_all_counts))