import sys
import os

init_pyscript = """
import re

QUESTION = '\033[94m'
ENDC = '\033[0m'

if __name__ == "__main__":
    seating_chart_p1 = []
    directory = re.sub("\/.*", "", __file__)
    with open(f'{directory}/test.txt', 'r') as infile:
        for line in infile:
            value = line.replace('\\n', '')
            seating_chart_p1.append(value)
"""

directory_name = sys.argv[1]

if os.path.exists(directory_name):
    print(f"{directory_name} directory already exists.")
else:
    os.makedirs(directory_name)
    with open(f"{directory_name}/{directory_name}.py", "w") as pyfile:
        pyfile.write(init_pyscript)
    open(f"{directory_name}/input.txt", "w").close()
    open(f"{directory_name}/test.txt", "w").close()

