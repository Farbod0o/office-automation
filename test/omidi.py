from model.entity import InventoryProduct
from model.entity.inventory import Inventory
from controller.controller import Controller, InventoryController, InventoryProductController

# status , inv = InventoryController.add_inventory("sandali","address","0912782347")
# print(inv.__dict__)
# inv = Controller.find_by_id(Inventory,2)
# status , pr = InventoryProductController.add_inventory_product("5",inv)

pr = Controller.find_by_id(InventoryProduct,4)
print(pr.inv_id.title)