from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.da.data_access import Base
from model.tools.validator import Validator, pattern_validator


class Department(Base):
    __tablename__ = "organization_tbl"
    _code = Column("organization_code", Integer, primary_key=True, autoincrement=True)
    _name = Column("organization_name", String(20), nullable=False, unique=True)
    _slogan = Column("organization_slogan", String(20), nullable=False, unique=True)
    _logo = Column("organization_logo", String(20), nullable=False, unique=True)
    _duties = Column("organization_duties", String(100), nullable=False, unique=False)
    _address = Column("organization_address", String(20), nullable=False, unique=True)
    _telephone = Column("organization_telephone", String(20), nullable=False, unique=True)
    _head_id = Column("head_id",Integer(10), nullable=True)
    _description = Column("organization_description", String(20), nullable=False, unique=False)

    def __init__(self, name, head):
        self.id = None
        self.name = name
        self.head_id = head.id

    def __repr__(self):
        return f"{self.__dict__}"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    @pattern_validator(r"^.{2,30}$","Invalid Department Name")
    def name(self, name):
        self._name = name

    @property
    def head_id(self):
        return self._head_id

    @head_id.setter
    def head_id(self, head_id):
        self._head_id = head_id


