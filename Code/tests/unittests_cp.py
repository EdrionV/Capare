import unittest
from scripts.inventory_cp import Inventory



class loadinventorytests(unittest.TestCase):
    def setUp(self):
        self.Inventory = Inventory()

    def test_loadinventory(self):
        inven = []
        x = "knife"
        load = self.Inventory.load_inventory(inven, x)
        self.assertEqual(load[len(load)-1], "knife")


class deleteinventorytests(unittest.TestCase):
    def setUp(self):
        self.Inventory = Inventory()

    def test_delinventory(self):
        inven = ["knife", "katana"]
        x = "knife"
        dele = self.Inventory.del_inventory(inven, x)
        self.assertEqual(dele[len(dele)-1], "katana")



if __name__ == '__main__':
    unittest.main()
