from sqlalchemy import Column, Integer, String, ForeignKey
from model.da.data_access import Base
from model.tools.validator import pattern_validator

class Department(Base):
    __tablename__ = "department_tbl"
    _code = Column("department_code", Integer, primary_key=True, autoincrement=True)
    _name = Column("department_name", String(30), nullable=False, unique=True)
    #parent_department = Column("parent_department_id", Integer, nullable=True)
    _duties = Column("department_duties", String(100), nullable=False)
    _department_location = Column("department_location", String(100), nullable=False, unique=False)
    _phone_number = Column("organization_phone_number", String(11), nullable=False, unique=False)
    _extension_number = Column("extension_number", String(11), nullable=False, unique=False)
    _access_level  = Column("access_level", String(15), nullable=False, unique=False)
    # _head_id = Column("head_id", Integer, nullable=True)
    # deputy_id = Column("deputy_id", Integer, nullable=True)
    _description = Column("department_description", String(100), nullable=False)

    def __init__(self, name, duties, location, phone_number,extension,access_lvl, description=""):
        self.name = name
        # self.parent_department = parent_department.code
        self.duties = duties
        self.department_location = location
        self.phone_number = phone_number
        self.extension_number = extension
        self.access_level = access_lvl
        #self._head_id = head_id
        # deputy_id = deputy_id
        self.description = description

    # Property for code
    @property
    def code(self):
        return self._code

    # Property for name
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
    @pattern_validator(r"^\d$", "شماره داخلی دپارتمان معتبر نیست!")
    def extension_number(self, value):
        self._extension_number = value
        
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    @pattern_validator(r"^\d$", "شماره دپارتمان معتبر نیست!")
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
    def head_id(self):
        return self._head_id

    @head_id.setter
    def head_id(self, value):
        self._head_id = value


    @property
    def deputy_id(self):
        return self._deputy_id

    @head_id.setter
    def deputy_id(self, value):
        self._deputy_id = value


    @property
    def description(self):
        return self._description

    @description.setter
    @pattern_validator(r"^.{2,100}$", "توضیحات دپارتمان معتبر نیست!")
    def description(self, value):
        self._description = value
