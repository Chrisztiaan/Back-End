class Person():
    # Class attributes
    home_planet = 'earth'
    species = 'humanity'

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

# Create new instance
alice = Person('Alice', 20)

# Access class and instance attributes
print(alice.home_planet)
print(alice.age)

if __name__ == "__main__":