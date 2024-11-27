from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship


class Section(Base):
    __tablename__ = "section_tbl"

    _id = Column("section_code", Integer, primary_key=True, autoincrement=True)
    _name = Column("section_name", String(30), nullable=False, unique=True)
    _address = Column("section_location", String(100), nullable=False)
    _phone_number = Column("section_phone_number", String(11), nullable=False)
    _internal_code = Column("internal_code", String(11), nullable=False)
    _access_level = Column("access_level", String(15), nullable=False)
    _parent_section_id = Column(Integer, ForeignKey("section_tbl.section_code"), nullable=True)
    _description = Column("section_description", String(100), nullable=False)
    _department_id = Column(Integer, ForeignKey("department_tbl._id"), nullable=True)
    parent_section = relationship("Section", remote_side=[_id], lazy='joined')
    dep_id = relationship("Department", back_populates="sections")

    def __init__(self, name, address, phone_number, internal_code, access_lvl, section_num, parent_section_num=None,
                 description=None,department=None):
        self._id = None
        self._name = name
        self._address = address
        self._phone_number = phone_number
        self._internal_code = internal_code
        self._description = description
        self._access_level = access_lvl
        self._section_num = section_num
        self._department_id = department._id
        self._parent_section_id = parent_section_num._id if parent_section_num else None

    @property
    def id(self):
        return self._id
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
    @pattern_validator(r"^.{2,30}$", "نام بخش معتبر نیست!")
    def name(self, name):
        self._name = name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def internal_code(self):
        return self._internal_code

    @internal_code.setter
    @pattern_validator(r"^\d{3}$", "کد داخلی بخش معتبر نیست!")
    def internal_code(self, value):
        self._internal_code = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    @pattern_validator(r"^\d{11}$", "شماره بخش معتبر نیست!")
    def phone_number(self, value):
        self._phone_number = value

    @property
    def access_level(self):
        return self._access_level

    @access_level.setter
    @pattern_validator(r"^.{2,15}$", "سطح دسترسی معتبر نیست!")
    def access_level(self, value):
        self._access_level = value

    @property
    def description(self):
        return self._description

    @description.setter
    @pattern_validator(r"^.{2,100}$", "توضیحات بخش معتبر نیست!")
    def description(self, value):
        self._description = value

    @property
    def section_code(self):
        return self._section_num

    @section_code.setter
    def section_code(self, value):
        self._section_num = value
