def roll_call_dwarves(list):
    for index, n in enumerate(list, start=1):
        print(f"{index}. {n}")

def summon_captain_planet(list):
    return [name.capitalize() + "!" for name in list]

def long_planeteer_calls(list):
    if len(list) == 4:
        return True
    elif len(list) >= 4:
        return False

def find_the_cheese(list):
    cheese_list = ["cheddar", "gouda", "camembert"]
    for cheese in list:
        if cheese in cheese_list:
            return cheese