from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, ForeignKey, DateTime)
from sqlalchemy.orm import relationship


class Inventory(Base):
    __tablename__ = "inventory_tbl"
    _id = Column("_id", Integer, primary_key=True, autoincrement=True)
    _title = Column("inventory_title", String(40))
    _address = Column("inventory_address", String(30))
    _phone = Column("inventory_phone", String(11))

    inventory_product = relationship("InventoryProduct", back_populates="inventory")

    def __init__(self, title, address, phone):
        self._id = None
        self._title = title
        self._address = address
        self._phone = phone

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    @pattern_validator(r"^.{2,20}$", "عنوان معتبر نیست")
    def title(self, title):
        self._title = title

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def phone(self):
        return self._phone

    @phone.setter
    @pattern_validator(r"^\d{11}$", "شماره تماس مورد نظر صحیح نمی باشد")
    def phone(self, phone):
        self._phone = phone
