# Do not modify these lines
from heapq import merge
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line

# Part 1: Create Passport


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality,
    }
    return passport


# print(create_passport("Chris", "19-04-1993", "Boskoop", 1.86, "Netherlands"))


# Part 2: Add Stamp

passport = {
    "name": "Chris",
    "date_of_birth": "19-04-1993",
    "place_of_birth": "Boskoop",
    "height": 1.86,
    "nationality": "Netherlands",
    "stamps": ["Luxembourg"],
}


def add_stamp(passport, country):
    if passport["nationality"] == country:
        return passport
    elif "stamps" not in passport:
        passport["stamps"] = [country]
        return passport
    else:
        if country in passport["stamps"]:
            return passport
        else:
            passport["stamps"].append(country)
            return passport


# print(add_stamp(passport, "Macao"))


# Part 3: Add Biometric Data


def add_biometric_data(passport, name_type, biometric_data, date_recorded):
    if name_type in passport["biometric"]:
        name_type = {"date": date_recorded, "value": biometric_data}
        return passport
    else:
        passport["biometric"][name_type] = {
            name_type: {"date": date_recorded, "value": biometric_data}
        }
        return passport


print(add_biometric_data(passport, "eye_color_middle", "blue", "28-04-2022"))
