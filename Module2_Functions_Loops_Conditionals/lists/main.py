# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

# 1

film_names = ["Valley of the dolls", "Superman",
              "The accidental tourist", "Lincoln", "Jaws"]  # etc


def alphabetical_order(film_names):
    return sorted(film_names)


print(alphabetical_order(film_names))


# 2

golden_globes = ["Jaws", "Star Wars: Episode IV - A New Hope",
                 "E.T. the Extra-Terrestrial", "Memoirs of a Geisha"]  # etc
film_name = "jaws"

# This will change all upper case letters in lower case for golden_globes
for i in range(len(golden_globes)):
    golden_globes[i] = golden_globes[i].lower()
# test print(golden_globes)


def won_golden_globe(film_name):
    if film_name in golden_globes:
        print(True)
    else:
        print(False)


won_golden_globe(film_name)


# 3

johns_list = ["Jaws", "Fahrenheit", "Star Wars: Episode IV - A New Hope", "E.T. the Extra-Terrestrial",
              'Old is New', "Memoirs of a Geisha", 'With a Little Help from My Friends']  # etc
josephs_albums = ["Fahrenheit", 'The Seventh One', 'Toto XX', 'Falling in Between', '35th Anniversary',
                  'Toto XIV', 'Old is New', '40 Tours Around the Sun', 'With a Little Help from My Friends']


def remove_toto_albums(johns_list):
    for i in johns_list:
        if i in josephs_albums:
            johns_list.remove(i)
    return johns_list


print(remove_toto_albums(johns_list))
