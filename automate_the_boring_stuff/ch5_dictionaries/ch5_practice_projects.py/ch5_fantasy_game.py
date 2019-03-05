
#? Fantasy Game Inventory
#? 1. Dictionaries: keys = item; values = num items;
#? 2. displayInventory() function: display inventory using pretty print module

import pprint

playerInventory = {'dagger': 2, 'gold': 42, 'torch': 2}

def displayInventory(inventory): 
    print('\nInventory:')
    item_total = 0 #? Initialize var to total up all items in inventory
    for k, v in inventory.items():
        item_total += v
        print(str(v) + ' ' + k)
    print('The total number of items: ' + str(item_total) + '\n')
displayInventory(playerInventory)
        