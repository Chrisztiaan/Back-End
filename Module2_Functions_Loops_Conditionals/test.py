golden_globes = ["Jaws", "Star Wars: Episode IV - A New Hope",
                 "E.T. the Extra-Terrestrial", "Memoirs of a Geisha"]


def won_golden_globe(check_golden_globe):
    if check_golden_globe in golden_globes:
        print(True)
        print(check_golden_globe.lower())
    else:
        print(False)


won_golden_globe("Star Wars: Episode IV - A New Hope")
golden_globes_corrupted = ["Jaws", "Fahrenheit", "Star Wars", "Episode IV - A New Hope",
                           "Toto XX", "E.T. the Extra-Terrestrial", "Memoirs of a Geisha"]
remove_toto_albums = ["Fahrenheit", "The Seventh One", "Toto XX", "Falling in Between", "35th Anniversary - Live in Poland", "Toto XIV",
                      "Old Is New", "40 Tours Around the Sun", "With a Little Help from My Friends"]
# #This will remove the items from list 'alphabetical_order' that are already in list 'remove_toto_albums'
for item in remove_toto_albums:
    if item in golden_globes_corrupted:
        golden_globes_corrupted.remove(item)
        print(golden_globes_corrupted)
