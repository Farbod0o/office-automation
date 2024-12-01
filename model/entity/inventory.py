from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, ForeignKey, DateTime)
from sqlalchemy.orm import relationship


class Inventory(Base):
    __tablename__ = "inventory"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _title = Column(String(40))
    _address = Column(String(30))
    _phone = Column(String(11))

    def __init__(self, title, address, phone):
        self._id = None
        self._title = title
        self._address = address
        self._phone = phone

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def title(self):
        return self._title

    @title.setter
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
    def phone(self, phone):
        self._phone = phone
