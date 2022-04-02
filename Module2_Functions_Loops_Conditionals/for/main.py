
from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

# 1


def shortest_names(countries):
    shortest = (min(countries, key=len))
    shortest_names = []

    for country in countries:
        if len(country) == len(shortest):
            shortest_names.append(country)

    return(shortest_names)


print(shortest_names(countries))


# 2

def most_vowels(countries):
    vowels = 'aeiou'
    top_countries = []
    top_countries_final = []

    for country in countries:
        vowels = 0
        for letter in country:
            if letter.lower() in country:
                vowels += 1

        top_countries.append([vowels, country])
        top_countries.sort(reverse=True)

    for list in top_countries[:4]:
        top_countries_final.append(list[1])

    return top_countries_final


print(most_vowels(countries))


# 3

def alphabet_set(countries):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = []
    alphabet_countries = []

    for country in countries:
        for letter in alphabet:
            if letter.lower() in country:
                if letter.lower() not in alphabet_list:
                    alphabet_list.append(letter)
                    if country not in alphabet_countries:
                        alphabet_countries.append(country)

    return alphabet_countries


print(alphabet_set(countries))
# print(len(alphabet_set(countries)))
