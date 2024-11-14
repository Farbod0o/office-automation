from sqlalchemy import Column, Integer, String, ForeignKey
from model.da.data_access import Base
from model.tools.validator import pattern_validator

class Organization(Base):
    __tablename__ = "organization_tbl"
    _code = Column("organization_code", Integer, primary_key=True, autoincrement=True)
    _name = Column("organization_name", String(30), nullable=False, unique=True)
    _slogan = Column("organization_slogan", String(50), nullable=False, unique=False)
    _logo = Column("organization_logo", String(20), nullable=False, unique=False)
    _duties = Column("organization_duties", String(100), nullable=False)
    _address = Column("organization_address", String(100), nullable=False, unique=False)
    _telephone = Column("organization_telephone", String(11), nullable=False, unique=False)
    # _head_id = Column("head_id", Integer, nullable=True)
    _description = Column("organization_description", String(100), nullable=False)

    def __init__(self, name, slogan, logo, duties, address, telephone, description=""):
        self.name = name
        self.slogan = slogan
        self.logo = logo
        self.duties = duties
        self.address = address
        self.telephone = telephone
        #self._head_id = head_id
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
    @pattern_validator(r"^.{2,30}$", "نام سازمان معتبر نیست!")
    def name(self, name):
        self._name = name

    # Property for slogan
    @property
    def slogan(self):
        return self._slogan

    @slogan.setter
    @pattern_validator(r"^.{2,50}$", "شعار سازمان معتبر نیست!")
    def slogan(self, value):
        self._slogan = value

    # Property for logo
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value

    # Property for duties
    @property
    def duties(self):
        return self._duties

    @duties.setter
    @pattern_validator(r"^.{2,100}$", "شرح وظایف سازمان معتبر نیست!")
    def duties(self, value):
        self._duties = value

    # Property for address
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    # Property for telephone
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    @pattern_validator(r"^\d{11}$", "شماره سازمان معتبر نیست!")
    def telephone(self, value):
        self._telephone = value

    # Property for head_id
    @property
    def head_id(self):
        return self._head_id

    @head_id.setter
    def head_id(self, value):
        self._head_id = value

    # Property for description
    @property
    def description(self):
        return self._description

    @description.setter
    @pattern_validator(r"^.{2,100}$", "توضیحات سازمان معتبر نیست!")
    def description(self, value):
        self._description = value
