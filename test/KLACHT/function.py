import json
import os
import random


def random_complaint():
    module_path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data_fp = open(os.path.join(module_path, "klacht.json"))
    facts = json.load(data_fp)
    return random.choice(facts)


print(random_complaint())
