class Inventory:

    def load_inventory(inventory, x):
        return inventory.append(x)

    def view_inventory(inventory):
        for i in range(len(inventory)):
            # print(i)
            print("Your equipment: ")
            print(inventory[i])

# #var = []
# Inventory.load_inventory("bag")
# Inventory.load_inventory("cot")
#
# #var = inventory
# Inventory.view_inventory()
# #print(var)
# Inventory.load_inventory("duf")
#
# Inventory.load_inventory("saf")
# Inventory.view_inventory()
#
# #print(var)
