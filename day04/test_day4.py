import unittest

from day4 import has_required_fields
from day4 import year_check
from day4 import height_check
from day4 import hair_color_check
from day4 import eye_color_check
from day4 import passport_id_check
from day4 import has_valid_values

class TestDay4(unittest.TestCase):
    def test_has_required_fields(self):
        self.assertTrue(has_required_fields('eyr:2021 hgt:168cm hcl:#fffffd pid:180778832 byr:1923 ecl:amb iyr:2019 cid:241'))
        self.assertTrue(has_required_fields('eyr:2021 hgt:168cm hcl:#fffffd pid:180778832 byr:1923 ecl:amb iyr:2019'))

    def test_doesnt_have_required_fields(self):
        self.assertFalse(has_required_fields('hgt:168cm hcl:#fffffd pid:180778832 byr:1923 ecl:amb iyr:2019 cid:241'))
        self.assertFalse(has_required_fields('eyr:2021 hcl:#fffffd pid:180778832 byr:1923 ecl:amb iyr:2019 cid:241'))
        self.assertFalse(has_required_fields('eyr:2021 hgt:168cm pid:180778832 byr:1923 ecl:amb iyr:2019 cid:241'))
        self.assertFalse(has_required_fields('eyr:2021 hgt:168cm hcl:#fffffd byr:1923 ecl:amb iyr:2019 cid:241'))
        self.assertFalse(has_required_fields('eyr:2021 hgt:168cm hcl:#fffffd pid:180778832 ecl:amb iyr:2019 cid:241'))
        self.assertFalse(has_required_fields('eyr:2021 hgt:168cm hcl:#fffffd pid:180778832 byr:1923 iyr:2019 cid:241'))
        self.assertFalse(has_required_fields('eyr:2021 hgt:168cm hcl:#fffffd pid:180778832 byr:1923 ecl:amb cid:241'))

    def test_passes_year_check(self):
        self.assertTrue(year_check('1980', 1920, 2002))
        self.assertTrue(year_check('2010', 2010, 2020))
        self.assertTrue(year_check('2030', 2020, 2030))

    def test_fails_year_check(self):
        self.assertFalse(year_check('2003', 1920, 2002))
        self.assertFalse(year_check('2009', 2010, 2020))

    def test_passes_height_check(self):
        self.assertTrue(height_check("60in"))
        self.assertTrue(height_check("190cm"))

    def test_fails_height_check(self):
        self.assertFalse(height_check("190in"))
        self.assertFalse(height_check("190"))

    def test_passes_haircolor_check(self):
        self.assertTrue(hair_color_check("#123abc"))

    def test_fails_haircolor_check(self):
        self.assertFalse(hair_color_check("123abc"))
        self.assertFalse(hair_color_check("#123abz"))

    def test_passes_eyecolor_check(self):
        self.assertTrue(eye_color_check('brn'))

    def test_fails_eyecolor_check(self):
        self.assertFalse(eye_color_check('wat'))

    def test_passes_pid_check(self):
        self.assertTrue(passport_id_check("000000001"))
        
    def test_fails_pid_check(self):
        self.assertFalse(passport_id_check("0123456789"))

    def test_has_valid_values(self):
        self.assertTrue(has_valid_values("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f"))
        self.assertTrue(has_valid_values("eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm"))
        self.assertTrue(has_valid_values("hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022"))
        self.assertTrue(has_valid_values("iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"))

    def test_doesnt_have_valid_values(self):
        self.assertFalse(has_valid_values("eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926"))
        self.assertFalse(has_valid_values("iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946"))
        self.assertFalse(has_valid_values("hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277"))
        self.assertFalse(has_valid_values("hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007"))

if __name__ == "__main__":
    unittest.main()