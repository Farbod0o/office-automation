from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, ForeignKey, DateTime)
from sqlalchemy.orm import relationship


class InventoryProduct(Base):
    __tablename__ = "inventory_product_tbl"

    _id = Column("_id", Integer, primary_key=True, autoincrement=True)
    _count = Column("product_inventory_count", Integer)
    _inventory_id = Column("inventory_id", Integer, ForeignKey("inventory_tbl._id"))
    _inventory_transaction_id = Column("inventory_transaction_id", Integer, ForeignKey("inventory_transaction_tbl._id"))

    inventory = relationship("Inventory", lazy="joined")
    inventory_transaction = relationship("InventoryTransaction", back_populates="inventory_product", lazy="joined")

    def __init__(self, count, inventory, inventory_transaction):
        self.id = None
        self.count = count
        self.inventory_id = inventory.id
        self.inventory_transaction_id = inventory_transaction.id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def count(self):
        return self._count

    @count.setter
    @pattern_validator(r"^\d+$", "")
    def count(self, count):
        self._count = count

