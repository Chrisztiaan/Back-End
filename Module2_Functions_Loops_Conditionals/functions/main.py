# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

# 1
def greet(name):
    return f"Hello, {name}!"

print(greet("Bob"))

# 2
def add(number_1, number_2, number_3):
    sum = number_1 + number_2 + number_3
    return sum

print(add(5,3,2))

# 3
def positive(number_positive):
    positive_check = number_positive > 0
    return positive_check

print(positive(-30))

# 4
def negative(number_negative):
    negative_check = number_negative < 0
    return negative_check

print(negative(4.39))

