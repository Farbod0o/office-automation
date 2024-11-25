from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, ForeignKey, DateTime)
from sqlalchemy.orm import relationship


class Delivery(Base):
    __tablename__ = "delivery"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _address = Column(String(50))
    _tracking_number = Column(String)
    # _cost =
    # _status =
    # _delivery_method =
    _shipped_date = Column(DateTime)
    _delivery_time = Column(DateTime)

    def __init__(self, address, tracking_number, shipped_date, delivery_time):
        self._address = address
        self._tracking_number = tracking_number
        self._shipped_date = shipped_date
        self._delivery_time = delivery_time

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def tracking_number(self):
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, tracking_number):
        self._tracking_number = tracking_number

    @property
    def shipped_date(self):
        return self._shipped_date

    @shipped_date.setter
    def shipped_date(self, shipped_date):
        self._shipped_date = shipped_date

    @property
    def delivery_time(self):
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, delivery_time):
        self._delivery_time = delivery_time
