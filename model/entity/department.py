from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = "department_tbl"

    _id = Column("department_code", Integer, primary_key=True, autoincrement=True)
    _name = Column("department_name", String(30), nullable=False, unique=True)
    _duties = Column("department_duties", String(100), nullable=False)
    _department_location = Column("department_location", String(100), nullable=False)
    _phone_number = Column("department_phone_number", String(11), nullable=False)
    _extension_number = Column("extension_number", String(11), nullable=False)
    _access_level = Column("access_level", String(15), nullable=False)
    _manager_id = Column(Integer, ForeignKey("person_tbl._id"), nullable=True)
    _deputy_id = Column(Integer, ForeignKey("person_tbl._id"), nullable=True)
    _parent_department_id = Column(Integer, ForeignKey("department_tbl.department_code"), nullable=True)
    _description = Column("department_description", String(100), nullable=False)

    manager = relationship("Person", foreign_keys=[_manager_id], lazy='joined')
    deputy = relationship("Person", foreign_keys=[_deputy_id], lazy='joined')
    parent_department = relationship("Department", remote_side=[_id], lazy='joined')



    def __init__(self, name, duties, location, phone_number, extension, access_lvl, description="", manager=None, deputy=None, parent_department=None):
        self._id = None
        self._name = name
        self._duties = duties
        self._department_location = location
        self._phone_number = phone_number
        self._extension_number = extension
        self._access_level = access_lvl
        self._description = description

        self._manager_id = manager.id if manager else None
        self._deputy_id = deputy.id if deputy else None
        self._parent_department_id = parent_department._id if parent_department else None


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
    @pattern_validator(r"^.{2,30}$", "نام دپارتمان معتبر نیست!")
    def name(self, name):
        self._name = name


    @property
    def duties(self):
        return self._duties

    @duties.setter
    @pattern_validator(r"^.{2,100}$", "شرح وظایف دپارتمان معتبر نیست!")
    def duties(self, value):
        self._duties = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value


    @property
    def extension_number(self):
        return self._extension_number
    
    @extension_number.setter
    @pattern_validator(r"^\d{3}$", "شماره داخلی دپارتمان معتبر نیست!")
    def extension_number(self, value):
        self._extension_number = value
        
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    @pattern_validator(r"^\d{11}$", "شماره دپارتمان معتبر نیست!")
    def phone_number(self, value):
        self._phone_number = value


    @property
    def access_level(self):
        return self._access_level

    @access_level.setter
    @pattern_validator(r"^.{2,15}$", "نام دپارتمان معتبر نیست!")
    def access_level(self, value):
        self._access_level = value

    @property
    def department_location(self):
        return self._department_location

    @department_location.setter
    @pattern_validator(r"^.{2,100}$", "مکان دپارتمان معتبر نیست!")
    def department_location(self, value):
        self._department_location = value

    @property
    def manager(self):
        return self._manager

    @manager.setter
    def manager(self, value):
        self._manager = value


    @property
    def deputy_id(self):
        return self._deputy_id

    @deputy_id.setter
    def deputy_id(self, value):
        self._deputy_id = value


    @property
    def description(self):
        return self._description

    @description.setter
    @pattern_validator(r"^.{2,100}$", "توضیحات دپارتمان معتبر نیست!")
    def description(self, value):
        self._description = value
