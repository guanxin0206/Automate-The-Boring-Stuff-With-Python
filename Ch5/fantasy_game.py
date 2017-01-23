# fantasyGame.py
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    # your code goes here
    for item in addedItems:
        inventory[item] = inventory.get(item,0) + 1
    return inventory

def displayInventory(inv):
    print("Inventory:")
    for k,v in inv.items():
        print(str(v) + " " + str(k))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
