from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, ForeignKey,DATETIME)
from sqlalchemy.orm import relationship

class Ticket(Base):
    __tablename__ = "ticket_tbl"
    _id = Column("ticket_id", Integer, primary_key=True, autoincrement=True)
    _userID = Column("user_id", Integer, ForeignKey("person_tbl._id"), nullable=False)
    _title = Column("department_title", String(30), nullable=False, unique=True)
    _ticket_datetime = Column("department_duties", DATETIME, nullable=False)
    _response_type = Column("response_type", String(30), nullable=False)
    _group = Column(Integer, ForeignKey("group_tbl._id"), nullable=True)

    user = relationship("Person", foreign_keys=[_userID], lazy='joined')
    gp = relationship("Group", foreign_keys=[_group], lazy='joined')


    def __init__(self,user, title, ticket_datetime, group, response_type):
        self._id = None
        self._userID = user.id
        self._title = title
        self._ticket_datetime = ticket_datetime
        self._response_type = response_type
        self._group = group.id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def userID(self):
        return self._userID

    @userID.setter
    def userID(self, value):
        self._userID = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def ticket_datetime(self):
        return self._ticket_datetime

    @ticket_datetime.setter
    def ticket_datetime(self, value):
        self._ticket_datetime = value

    @property
    def response_type(self):
        return self._response_type

    @response_type.setter
    def response_type(self, value):
        self._response_type = value

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value

