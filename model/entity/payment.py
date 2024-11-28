from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, DateTime, func)
from sqlalchemy.orm import relationship


class Payment(Base):
    __tablename__ = "payment_tbl"
    _id = Column("payment_id", Integer, primary_key=True, autoincrement=True)
    _doc_number = Column("doc_number", String(30), nullable=False, unique=True)
    _date =Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    _description = Column("description", String(300), nullable=False)
    transaction = relationship("Transaction", back_populates="payment")


    def __init__(self, doc_number, description):
        self._id = None
        self._doc_number = doc_number
        self._description = description

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def doc_number(self):
        return self.doc_number

    @doc_number.setter
    @pattern_validator(r"^.{2,30}$", "نام دپارتمان معتبر نیست!")
    def name(self, doc_number):
        self._doc_number = doc_number

    @property
    def date(self):
        return self._date

    @date.setter
    @pattern_validator(r"^.{2,100}$", "شرح وظایف دپارتمان معتبر نیست!")
    def duties(self, date):
        self._date = date

    @property
    def description(self):
        return self._description

    @description.setter
    def address(self, value):
        self._description = value

