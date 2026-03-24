import random
import os
import sys

def clear(): #cls for win and clear for linux, apparently it'll show error code if i kept use "cls;clear"
	if sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")


# ==============================================================================
# NOTE FOR SELF
# the for item, qty is the same as list 0, 1(the first and the second)
# basically for (variable name) in (data)
# u can put anything like, for uwu, ewe in player
# because uwu and ewe is just a variable name,
# the uwu takes the first index(0)
# and the second takes the second index(1)
# thus itll be for (name), (1) in player
# it's 1 because remember the line 50-54!
# it gives value of the name
# like, it became 
# uwu = rock
# ewe = 1
# ===============================================================================


def show_plr(player):
    clear()
    print(f"{'Name':<10} : {player['name']}")
    print(f"{'Uid':<10} : {player['uid']}")
    print(f"{'Money':<10} : {player['money']}")
    item_list = []
    for item, qty in player["inventory"].items():
        item_list.append(f"{item} (x{qty})")
    items = ", ".join(item_list) if player["inventory"] else "None"
    print(f"{'items':<10} : {items}")

def get_item(drop):
    result = []
    chance = random.randint(1, 100)
    if chance <= 60:
        rarity = "common"
    else:
        rarity = "rare"
    
    # get all the items in the drops,
    # and put all the items in result
    for item in drop:
        if item["rarity"] == rarity:
            result.append(item)
    
    picked = random.choice(result)
    clear()
    print(f"congrats! you got a {picked['rarity']} {picked['name']}!")
    item_name = picked["name"]

# basically checking if the item is already in inventory
# if yes, add 1 upvalue
# if not, = 1 to add it, to make it exist
    if item_name in player["inventory"]:
        player["inventory"][item_name] += 1
    else:
        player["inventory"][item_name] = 1

def interface():
    clear()
    while True:
        print("""
    [1] Show Player Data
    [2] Get Items
    [3] Exit
""")
        x = input()
        if x == "1":
            show_plr(player)
        elif x == "2":
            get_item(drop)
        elif x == "3":
            break




#==========PLAYER==========
player = {
    "name" : None,
    "uid" : 0,
    "money" : 0,
    "inventory" : {}
}
uid_gen = 800000000 + random.randint(100, 999999)
player["uid"] = uid_gen
#==========================
drop = [
    {"name": "rock", "rarity": "common"},
    {"name": "stone", "rarity": "common"},
    {"name": "sword", "rarity": "rare"},
    {"name": "longsword", "rarity": "rare"},
]
#==========================

interface()