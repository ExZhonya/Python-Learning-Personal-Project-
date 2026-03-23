import random
import os


def show_plr(player):
    print(f"{'Name':<10} : {player['name']}")
    print(f"{'Uid':<10} : {player['uid']}")
    print(f"{'Money':<10} : {player['money']}")
    items = ", ".join(player["inventory"].keys()) if player["inventory"] else "None"
    print(f"{'items':<10} : {items}")

def get_item(drop):
    result = []
    chance = random.randint(1, 100)
    if chance <= 60:
        rarity = "common"
    else:
        rarity = "rare"
    
    for item in drop:
        if item["rarity"] == rarity:
            result.append(item)
    
    picked = random.choice(result)
    print(f"congrats! you got a {picked['rarity']} {picked['name']}!")
    item_name = picked["name"]

    inv = player["inventory"]
    if item_name in inv:
        inv[item_name] += 1
    else:
        inv[item_name] = 1

#==========PLAYER==========
player = {
    "name" : None,
    "uid" : None,
    "money" : 0,
    "inventory" : {}
}
#==========================
drop = [
    {"name": "rock", "rarity": "common"},
    {"name": "stone", "rarity": "common"},
    {"name": "sword", "rarity": "rare"},
    {"name": "longsword", "rarity": "rare"},
]
#==========================

show_plr(player)
get_item(drop)
show_plr(player)