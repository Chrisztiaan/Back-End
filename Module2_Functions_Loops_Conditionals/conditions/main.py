# Do not modify these lines
__winc_id__ = "25596924dffe436da9034d43d0af6791"
__human_name__ = "conditions"

# Add your code after this line


def farm_action(
    weather,
    time_of_day,
    cow_milking_status,
    location_of_cows,
    season,
    slurry_tank,
    grass_status,
):
    if location_of_cows == "pasture" and time_of_day == "night":
        return "take cows to cowshed"
    elif location_of_cows == "pasture" and weather == "rainy":
        return "take cows to cowshed"
    elif cow_milking_status == True and location_of_cows == "cowshed":
        return "milk cows"
    elif cow_milking_status == True and location_of_cows == "pasture":
        return "take cows to cowshed\nmilk cows\ntake cows back to pasture"
    elif (
        slurry_tank == True
        and location_of_cows == "cowshed"
        and weather != "sunny"
        and weather != "windy"
    ):
        return "fertilize pasture"
    elif (
        slurry_tank == True
        and location_of_cows == "pasture"
        and weather != "sunny"
        and weather != "windy"
    ):
        return "take cows to cowshed\nfertilize pasture\ntake cows back to pasture"
    elif (
        grass_status == True
        and season == "spring"
        and weather == "sunny"
        and location_of_cows != "pasture"
    ):
        return "mow grass"
    elif (
        grass_status == True
        and season == "spring"
        and weather == "sunny"
        and location_of_cows == "pasture"
    ):
        return "take cows to cowshed\nmow grass\ntake cows back to pasture"
    else:
        return "wait"


print(farm_action("rainy", "night", False, "cowshed", "winter", False, True))
