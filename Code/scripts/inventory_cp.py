class Inventory:

    def load_inventory(self, inventory, x):
        # inventory.append(x)
        return inventory.append(x)

    def view_inventory(self, inventory):
        print("Your equipment: ")
        for i in range(len(inventory)):
            print(inventory[i])

    def del_inventory(self, inventory, y):
        # inventory.remove(y)
        return inventory.remove(y)


