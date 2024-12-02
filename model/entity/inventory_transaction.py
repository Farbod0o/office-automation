from datetime import datetime
from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, ForeignKey, DATETIME)
from sqlalchemy.orm import relationship


class InventoryTransaction(Base):
    __tablename__ = "inventory_transaction_tbl"
    _id = Column("_id", Integer, primary_key=True, autoincrement=True)
    _count = Column("inventory_transaction_count", Integer, default=0)
    _date_time = Column(DATETIME)
    _status = Column(Enum)

    def __init__(self, count, date_time):
        self._id = None
        self._count = count
        self._date_time = date_time

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
    def count(self, count):
        self._count = count


    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        self._date_time = date_time
