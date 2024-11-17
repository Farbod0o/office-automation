from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, ForeignKey,DATETIME)
from sqlalchemy.orm import relationship

class Group(Base):
    __tablename__ = "group_tbl"
    _id = Column("_id", Integer, primary_key=True, autoincrement=True)
    _parent_group = Column("parent_group", Integer, ForeignKey("group_tbl._id"), nullable=True)
    _name = Column("name", String(30), nullable=False, unique=True)

    parent = relationship("Group", remote_side=[_id], lazy='joined')

    def __init__(self,name,parent_group=None):
        self._id = None
        self._name = name
        self._parent_group = parent_group.id if parent_group else None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self,value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    @property
    def parent_group(self):
        return self._parent_group

    @parent_group.setter
    def parent_group(self,value):
        self._parent_group = value
