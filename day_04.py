from helpers.utils import get_puzzle_input
import re

test_input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""


def check_height(hgt):
    if not hgt:
        return False
    if hgt[-2:] not in {"cm", "in"}:
        return False
    height_value = int(hgt[:-2])
    if hgt[-2:] == "in":
        if height_value >= 59 and height_value <= 76:
            return True
    if hgt[-2:] == "cm":
        if height_value >= 150 and height_value <= 193:
            return True
    return False


def check_pid(pid):
    if len(pid) != 9:
        return False
    try:
        int(pid)
        return True
    except ValueError as e:
        return False


count = 0
count_p2 = 0
for passport in get_puzzle_input(4, is_viv=True).split("\n\n"):
# for passport in test_input.split("\n\n"):
    key_value_dict = {}
    passport_info = passport.split()
    for passport_info_bit in passport_info:
        key, value = passport_info_bit.split(":")
        if key in ["byr", "eyr", "iyr"]:
            value = int(value)
        key_value_dict[key] = value
    if len(key_value_dict) == 8:
        count += 1
    elif len(key_value_dict) == 7 and "cid" not in key_value_dict:
        count += 1
    if all([

        1920 <= key_value_dict.get("byr", 0) <= 2002,
        2010 <= key_value_dict.get("iyr", 0) <= 2020,
        2020 <= key_value_dict.get("eyr", 0) <= 2030,
        check_height(key_value_dict.get("hgt", None)),
        re.match(r"^#[0-9a-f]{6}$", key_value_dict.get("hcl", "")),
        key_value_dict.get("ecl", "") in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        check_pid(key_value_dict.get("pid", "")),

    ]):
        print("valid")
        count_p2 += 1
    else:
        print("invalid")
print(count_p2)
