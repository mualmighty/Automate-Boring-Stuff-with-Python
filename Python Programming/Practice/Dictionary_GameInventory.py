"""
Fantasy Game Inventory
You are creating a fantasy video game.
The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detail- ing how many of that item the player has.
For example, the dictionary value:
    {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.

Write a function named displayInventory() that would take any possible “inventory” and display it like the following:
             Inventory:
             12 arrow
             42 gold coin
             1 rope
             6 torch
             1 dagger
             Total number of items: 62
"""

def displayInventory(**kwargs):
    print("Inventory: ")
    count = 0
    for k,v in kwargs.items():
        print(v, k)
        count += v
    print('Total number of items: %d' %count)



if __name__ == '__main__':
    stuffs = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    displayInventory(**stuffs)




