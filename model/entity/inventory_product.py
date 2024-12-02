from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, ForeignKey, DateTime)
from sqlalchemy.orm import relationship


class InventoryProduct(Base):
    __tablename__ = "inventory_product_tbl"

    _id = Column("_id", Integer, primary_key=True, autoincrement=True)
    _count = Column("product_inventory_count", Integer)

    def __init__(self, count):
        self._id = None
        self._count = count

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

