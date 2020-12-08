import os
import re
from pprint import pprint
QUESTION = '\033[94m'
ENDC = '\033[0m'

def traverse_instructions(instructions: list) -> int:
    """Traverse the instruction set and return the acc value of the initial loop."""
    seen_indices = list()
    current_index = 0
    acc_value = 0

    while current_index < len(instructions):
        if current_index in set(seen_indices):
            break

        seen_indices.append(current_index)
        current_instruction = instructions[current_index]
        
        if current_instruction['instruction'] == 'jmp':
            current_index += current_instruction['magnitude']
            continue

        if current_instruction['instruction'] == 'acc':
            acc_value += current_instruction['magnitude']

        current_index += 1
    
    return (acc_value, current_index>=len(instructions))


if __name__ == "__main__":
    instructions = []
    directory = re.sub("\/.*", "", __file__)
    with open(f'{directory}/input.txt', 'r') as infile:
        for line in infile:
            value = line.replace('\n', '')
            instructions.append({'instruction': value.split(" ")[0], 'magnitude': int(value.split(" ")[1].replace("+", ""))})

    # pprint(instructions)
    p1_acc_value, p1_exited_instructions = traverse_instructions(instructions)
    print(QUESTION+"Immediately before any instruction is executed a second time, what value is in the accumulator?"+ENDC)
    print(p1_acc_value)

    for index, instruction in enumerate(instructions):
        if instruction.get('instruction') == 'acc' or (instruction.get('instruction') == 'nop' and instruction.get('magnitude') == 0 and index == 0):
            continue
        
        temp_instruction_set = list(instructions)

        if instruction.get('instruction') == 'jmp':
            temp_instruction_set[index] = {"instruction": "nop", "magnitude": instruction.get("magnitude")}
        elif instruction.get('instruction') == 'nop':
            temp_instruction_set[index] = {"instruction": "jmp", "magnitude": instruction.get("magnitude")}

        p2_acc_value, p2_exited_instructions = traverse_instructions(temp_instruction_set)
        if p2_exited_instructions:
            print("P2 Exited!")
            break
    print(QUESTION+"Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?"+ENDC)
    print(p2_acc_value)