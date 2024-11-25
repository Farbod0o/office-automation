from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, ForeignKey, DateTime)
from sqlalchemy.orm import relationship


class InventoryProduct(Base):
    __tablename__ = "inventory_product"

    _id = Column(Integer, primary_key=True, autoincrement=True)
    _count = Column(Integer, default=0)

    def __init__(self, count):
        self._id = None
        self._count = count

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        self._count = count

