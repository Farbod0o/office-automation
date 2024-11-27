from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model.da.data_access import Base
from model.tools.validator import pattern_validator


class Department(Base):
    __tablename__ = "department_tbl"
    _id = Column("_id", Integer, primary_key=True, autoincrement=True)
    _name = Column("organization_name", String(30), nullable=False, unique=True)
    _logo = Column("organization_logo", String(20), nullable=False, unique=False)
    _address = Column("organization_address", String(100), nullable=False, unique=False)
    _phone_number = Column("organization_phone_number", String(11), nullable=False, unique=False)
    _department_num = Column("department_num", String(20), nullable=False, unique=False)
    _description = Column("organization_description", String(100), nullable=False)
    _task = Column("organization_task", String(100), nullable=False)
    sections = relationship("Section", back_populates="dep_id")

    def __init__(self, name, department_num, logo, task, address, phone_number, description=""):
        self._id = None
        self._name = name
        self._department_num = department_num
        self._logo = logo
        self._task = task
        self._address = address
        self._phone_number = phone_number
        self._description = description


    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    @pattern_validator(r"^.{2,30}$", "نام سازمان معتبر نیست!")
    def name(self, name):
        self._name = name

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value

    @property
    def task(self):
        return self._task

    @task.setter
    @pattern_validator(r"^.{2,100}$", "شرح وظایف سازمان معتبر نیست!")
    def task(self, value):
        self._task = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    @pattern_validator(r"^\d{11}$", "شماره سازمان معتبر نیست!")
    def phone_number(self, value):
        self._phone_number = value

    @property
    def description(self):
        return self._description

    @description.setter
    @pattern_validator(r"^.{2,100}$", "توضیحات سازمان معتبر نیست!")
    def description(self, value):
        self._description = value
