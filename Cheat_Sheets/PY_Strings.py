
# Adding an ' or " in a string

example_one = 'I\'m a string.'
example_two = "I'm a string."
example_three = 'He said: "I\'m a string"'

# Adding \ in a string: Use \\

stringtest = "I use ' in this string"
stringtest2 = 'I\'m not sure if this works'
stringtest3 = "and if i say test\\try do I get a single one?"
stringtest4 = 'This string \n Is special \t in it\'s own way'

print(stringtest)
print(stringtest2)
print(stringtest3)
print(stringtest4)

# Operators

# = + - == etc

print('Hello, ' + 'world!')
print('Jump! ' * 5)
print(5 * 'jummp')

# Membership operator in

print('Samuel' in 'We went out for dinner with with Anne, Samuel and Bob.') #True
print('Shane' in 'We went out for dinner with with Anne, Samuel and Bob.')  #True
print(5 in 'We were lucky that they had a table for 5.')                    #Error because 5 is int and not str
print(str(5) in 'We were lucky that they had a table for 5.')               #True


# Index

# 0,1,2,3,4 etc is index for a indication
waltz[start:stop:step]
len() #function to determine the length of a string

# f - strings
answer = 42
qa = f'The answer is.. {answer}'
print(qa)

# Slicing

waltz = 'onetwothree'
waltz[0:3]
# We don't need to specify the 0 if we start at the beginning
waltz[:3]
waltz[3:6]
print(waltz[6:11])
# Same goes for the end -- we can leave it empty
waltz[6:]
# We can specify a step size if we don't want a continuous slice
print(waltz[0:11:2])