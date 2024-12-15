from model.entity import InventoryProduct, InventoryTransaction
from model.entity.inventory import Inventory
from controller.controller import Controller, InventoryController, InventoryProductController, \
    InventoryTransactionController, DeliveryController


# ok
# inventory = InventoryController.add_inventory("qqq", "qqqqq", "09900909912")
# print(inventory)

# obj
# print(InventoryProductController.add_inventory_product(2, inventory, inventory_transaction))

# ok
status, inventory_transaction = InventoryTransactionController.add_inventory_transaction(5, "2010-12-12 12:11:00", "active")
print(inventory_transaction)

# obj
status, delivery = DeliveryController.add_delivery("dsd", "12", "2200", "active",
                                           "test", "2020-12-13 12:00:00",
                                           "2020-10-13 12:12:12", inventory_transaction)
print(delivery)