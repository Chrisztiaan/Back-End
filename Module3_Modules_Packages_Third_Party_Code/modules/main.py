# Do not modify these lines
__winc_id__ = "78029e0e504a49e5b16482a7a23af58c"
__human_name__ = "modules"

# Add your code after this line

# 1 All imports

# import this

import time
import math
import datetime
import sys
from greet import supergreeting

# 2


def wait(seconds):
    time.sleep(seconds)


# 3


def my_sin(float):
    sin = math.sin(float)
    return sin


# 4


def iso_now():
    now = datetime.datetime.now()
    str_now = now.strftime("%Y-%m-%dT%H:%M")
    return str_now


# 5


def platform():
    return sys.platform


# 6


def supergreeting_wrapper(name):
    return supergreeting(name)


print(supergreeting_wrapper("Eva"))
