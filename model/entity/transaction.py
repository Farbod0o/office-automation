from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship


class Transaction(Base):
    __tablename__ = "transaction_tbl"

    _id = Column("transaction_code", Integer, primary_key=True, autoincrement=True)
    #_payment_method =
    # _amount =
    # _date =
    _tracking_code =Column("tracking_code", Integer, primary_key=True, autoincrement=True)


    def __init__(self, payment_method, amount, date, tracking_code):
        self._id = None
        self._payment_method = payment_method
        self._amount = amount
        self._date = date
        self._trackingcode = tracking_code


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # @property
    # def _payment_method(self):
    #     return self._payment_method
    #
    # @_payment_method.setter
    # @pattern_validator(r"^.{2,30}$", "نام دپارتمان معتبر نیست!")
    # def _payment_method(self, _payment_method):
    #     self._payment_method = _payment_method
    #
    # @property
    # def _amount(self):
    #     return self._amount
    #
    # @_amount.setter
    # @pattern_validator(r"^.{2,100}$", "شرح وظایف دپارتمان معتبر نیست!")
    # def _amount(self, value):
    #     self._amount = value
    #
    # @property
    # def _date(self):
    #     return self._date
    #
    # @_date.setter
    # def _date(self, value):
    #     self._date = value

    @property
    def _tracking_code(self):
        return self._tracking_code

    @_tracking_code.setter
    @pattern_validator(r"^\d{3}$", "شماره داخلی دپارتمان معتبر نیست!")
    def _tracking_code(self, value):
        self._tracking_code = value

