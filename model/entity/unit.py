from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import Column, Integer, String


class Unit(Base):
    __tablename__ = "unit_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(30), nullable=False)
    _amount = Column("amount", Integer, nullable=False)
    _description = Column("description", String(200), nullable=False)

    def __init__(self, id, name, amount, description):
        self._id = None
        self._name = name
        self._amount = amount
        self._description = description

    @property
    def id(self):
        return self._id

    @id.setter
    @pattern_validator("^[0-9]$", " آیدی معتبر نیست!")
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("نام معتبر نیست!")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if isinstance(amount, int):
            self._amount = amount
        else:
            raise ValueError("تعداد معتبر نیست")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self._description = description

        else:
            raise ValueError("توضیحات معتبر نیست")




