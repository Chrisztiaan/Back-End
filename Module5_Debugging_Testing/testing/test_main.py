# Imports from main

from main import get_none
from main import flatten_dict

# Test functions


def test_get_none():
    assert get_none() == None


def test_flatten_dict():
    assert type(flatten_dict(
        {'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})) is list


# Execute tests

def main():
    print(test_get_none())
    print(test_flatten_dict())

main()
