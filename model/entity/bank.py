from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship


class Bank(Base):
    __tablename__ = "bank_tbl"
    _id = Column("bank_id", Integer, primary_key=True, autoincrement=True)
    _name = Column("bank_name", String(30), nullable=False, unique=True)
    _account_number = Column("account_number", String(30), nullable=False)
    _branch_code = Column("branch_code", Integer, nullable=False)
    trans = relationship("Transaction", back_populates="bnk")


    def __init__(self, name, account_number, branch_code):
        self._id = None
        self._name = name
        self._account_number = account_number
        self._branch_code = branch_code


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    @pattern_validator(r"^.{2,30}$", "نام بانک معتبر نیست!")
    def name(self, name):
        self._name = name

    @property
    def account_number(self):
        return self.account_number

    @account_number.setter
    @pattern_validator(r"^.{2,30}$", "شماره اکانت معتبر نیست!")
    def account_number(self, value):
        self.account_number = value

    @property
    def branch_code(self):
        return self.branch_code

    @branch_code.setter
    def branch_code(self, value):
        self.branch_code = value

