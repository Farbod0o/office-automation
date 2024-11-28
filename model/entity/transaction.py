from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, DateTime, Enum, Double, DATETIME, func, ForeignKey)
from sqlalchemy.orm import relationship


class Transaction(Base):
    __tablename__ = "transaction_tbl"

    _id = Column("transaction_code", Integer, primary_key=True, autoincrement=True)
    _payment_method = Column(Enum("PaymentMethod", "PaymentMethod2"), default="PaymentMethod", nullable=False, )
    _amount = Column(Integer, nullable=False)
    _date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    _tracking_code = Column("tracking_code", Integer, primary_key=True, autoincrement=True)
    _payment_id = Column(ForeignKey("payment_tbl.payment_id"), nullable=False)
    _bank_id = Column(ForeignKey("bank_tbl.bank_id"), nullable=False)

    bnk = relationship("Bank", back_populates="trans")
    payment = relationship("Payment", back_populates="transaction")

    def __init__(self, payment_method, amount, tracking_code, payment, bank):
        self._id = None
        self._payment_method = payment_method
        self._amount = amount
        self._trackingcode = tracking_code
        self._payment_id = payment._id
        self._bank_id = bank._id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def _tracking_code(self):
        return self._tracking_code

    @_tracking_code.setter
    @pattern_validator(r"^\d{3}$", "شماره داخلی دپارتمان معتبر نیست!")
    def _tracking_code(self, value):
        self._tracking_code = value
