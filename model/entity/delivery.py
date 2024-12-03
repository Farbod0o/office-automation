
from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, ForeignKey, DATETIME, Enum, Float)
from sqlalchemy.orm import relationship


class Delivery(Base):
    __tablename__ = "delivery_tbl"
    _id = Column("_id", Integer, primary_key=True, autoincrement=True)
    _address = Column("delivery_address", String(50))
    _tracking_number = Column("delivery_tracking_number", String(30))
    _cost = Column("delivery_cost", Float, nullable=False)
    _status = Column("delivery_status", Enum("active", "inactive", "pending"))
    _delivery_method = Column("delivery_method", Enum("one", "two", "three"))
    _shipped_date = Column(DATETIME)
    _delivery_time = Column(DATETIME)

    def __init__(self, address, tracking_number, cost, status, delivery_method, shipped_date, delivery_time):
        self._address = address
        self._tracking_number = tracking_number
        self._cost = cost
        self._status = status
        self._delivery_method = delivery_method
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
    @pattern_validator(r"^\d+$", "شماره پیگیری معتبر نمی باشد")
    def tracking_number(self, tracking_number):
        self._tracking_number = tracking_number

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        self._cost = cost

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def delivery_method(self):
        return self._delivery_method

    @delivery_method.setter
    def delivery_method(self, delivery_method):
        self._delivery_method = delivery_method

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
