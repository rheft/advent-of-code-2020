import re

QUESTION = '\033[94m'
ANSWER = '\033[93m'
ENDC = '\033[0m'

def format_data(entry: str) -> dict:
    """Method for extracting the information from the input string"""
    return {
        "string_value": entry.split(": ")[1],
        "target_letter": entry.split(": ")[0].split(" ")[1],
        "min_count": int(entry.split(": ")[0].split(" ")[0].split("-")[0]),
        "max_count": int(entry.split(": ")[0].split(" ")[0].split("-")[1]),
    }

def sled_rental_password_validation(password_data: dict) -> bool:
    """AoC day 2.a:
        Given a max and min integers and a target letter
        Determine if a string contains contains the target letter no less than the minimum and no more than the maximum
    """
    regex_string = f"[^{password_data['target_letter']}]"
    target_letter_occurences = len(re.sub(regex_string, "", password_data["string_value"]))
    return target_letter_occurences <= password_data["max_count"] and target_letter_occurences >= password_data["min_count"]

def toboggan_password_validation(password_data: dict) -> bool:
    """AoC day 2.b:
        Given a 2 indices and a target letter
        Determine if the target letter exists at EXACTLY one of those indices (-1 to reset the index)
    """
    position_A_match =int(password_data["target_letter"] == password_data["string_value"][password_data["min_count"]-1])
    position_B_match = int(password_data["target_letter"] == password_data["string_value"][password_data["max_count"]-1])
    return position_A_match+position_B_match==1

def valid_password_count(passwords: list, validation_function) -> int:
    return sum([1 if validation_function(password_data) else 0 for password_data in passwords])

if __name__ == "__main__":
    passwords = []
    with open('dayTwo/input.txt', 'r') as infile:
        for line in infile:
            value = line.replace('\n', '')
            processed_value = format_data(value)
            passwords.append(processed_value)

    sled_rental_valid_passwords = valid_password_count(passwords, sled_rental_password_validation)
    toboggan_valid_passwords = valid_password_count(passwords, toboggan_password_validation)

    print(QUESTION+"Problem A: \"How many passwords contain a designated letter the indicated number of times?\""+ENDC)
    print(ANSWER+"Answer: "+str(sled_rental_valid_passwords)+ENDC)
    print(QUESTION+"Problem A: \"How many passwords contain a desicnated letter at the specified indices\""+ENDC)
    print(ANSWER+"Answer: "+str(toboggan_valid_passwords)+ENDC)

    