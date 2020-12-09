import re

def has_required_fields(passport: str) -> bool:
    """Return True if we've got all the required fields."""
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    passport_fields = set([field.split(":")[0] for field in passport.split(" ")])
    return required_fields.issubset(passport_fields)

def year_check(year_value: str, min_value: int, max_value: int) -> bool:
    """Check if the year is valid"""
    return bool(re.search(r"\d{4}", year_value)) and int(year_value) >= min_value and int(year_value) <= max_value

def height_check(height_value: str) -> bool:
    """Check if the height value passes validation."""
    if bool(re.search(f"\dcm", height_value)) and int(height_value.lower().replace("cm" ,"")) >= 150 and int(height_value.lower().replace("cm" ,"")) <= 193:
        return True

    if bool(re.search(f"\din", height_value)) and int(height_value.lower().replace("in" ,"")) >= 59 and int(height_value.lower().replace("in" ,"")) <= 76:
        return True

    return False

def hair_color_check(hair_color_value: str) -> bool:
    """check if the hair color value passes validation."""
    return bool(re.search(r"^#([a-fA-F0-9]{6})", hair_color_value))

def eye_color_check(eye_color: str) -> bool:
    """check if the eye color value passes validation."""
    return eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def passport_id_check(passport_id: str) -> bool:
    """check if the passport id passes validation."""
    return bool(re.search(r"^\d{9}$", passport_id))

def has_valid_values(passport: str) -> bool:
    """Return True if the passport contains all valid fields and has valid values as well."""
    if not has_required_fields(passport):
        return False
    # create dictionary of passport data
    passport_data = {field.split(":")[0]: field.split(":")[1] for field in passport.split(" ") if field != ""}

    validity_checks = [
        year_check(year_value=passport_data['byr'], min_value=1920, max_value=2002), # Birth Year Check
        year_check(year_value=passport_data['iyr'], min_value=2010, max_value=2020), # Issue Year Check
        year_check(year_value=passport_data['eyr'], min_value=2020, max_value=2030), # Expiration Year Check
        height_check(height_value=passport_data['hgt']), # Height Check
        hair_color_check(hair_color_value=passport_data['hcl']), # Hair Color Check
        eye_color_check(eye_color=passport_data['ecl']), # Eye Color Check
        passport_id_check(passport_id=passport_data['pid']) # Passport ID Check
    ]

    return all(validity_checks)

if __name__ == "__main__":
    current_passport = ''
    required_fields = 0
    passes_validity_checks = 0
    with open('day4/input.txt', 'r') as infile:
        for line in infile:
            value = line.replace('\n', '')
            if value == '':
                contains_required_fields = has_required_fields(current_passport)
                passport_passes_validity_checks = has_valid_values(current_passport)
                required_fields += 1 if contains_required_fields else 0
                if not passport_passes_validity_checks:
                    print(current_passport)
                passes_validity_checks += 1 if passport_passes_validity_checks else 0
                # print(current_passport, contains_required_fields, passport_passes_validity_checks)
                current_passport = ''
            else:
                current_passport = " ".join([current_passport, value])

        # take care of the last entry
        contains_required_fields = has_required_fields(current_passport)
        passport_passes_validity_checks = has_valid_values(current_passport)
        required_fields += 1 if contains_required_fields else 0
        passes_validity_checks += 1 if passport_passes_validity_checks else 0
        print(current_passport, contains_required_fields, passport_passes_validity_checks)

    print(required_fields)
    print(passes_validity_checks)
            