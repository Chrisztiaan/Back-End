import keyword
print(keyword.kwlist)

def eligible_to_vote(age, nationality):
    if age >= 18 and nationality == 'Italian':
        print('Bene!')
        return True
    elif age >= 25 and nationality == 'Portuguese':
        print('Sim!')
        return True
    elif age >= 31 and nationality == 'Dutch':
        print('Top!')
        return True
    elif age >= 19 and nationality == 'Malawian':
        print('Iya!')
        return True
    else:
        return False