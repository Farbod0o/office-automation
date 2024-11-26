from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship


class Payment(Base):
    __tablename__ = "payment_tbl"
    _id = Column("payment_id", Integer, primary_key=True, autoincrement=True)
    _doc_number = Column("doc_number", String(30), nullable=False, unique=True)
    # _date
    _description = Column("description", String(300), nullable=False)


    def __init__(self, doc_number, date, description):
        self._id = None
        self._doc_number = doc_number
        self._date = date
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

