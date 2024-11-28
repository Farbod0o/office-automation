from model.da.data_access import Base
from model.tools.validator import pattern_validator
from sqlalchemy import (Column, String, Integer, ForeignKey, DATETIME)
from sqlalchemy.orm import relationship


class Ticket(Base):
    __tablename__ = "ticket_tbl"
    _id = Column("ticket_id", Integer, primary_key=True, autoincrement=True)
    # _userID = Column("user_id", Integer, ForeignKey("person_tbl._id"), nullable=False)
    _title = Column("department_title", String(30), nullable=False, unique=True)
    _ticket_datetime = Column(DATETIME)
    _response_type = Column("response_type", String(30), nullable=False)
    _text = Column("text", String(250), nullable=False)

    # _group = Column(Integer, ForeignKey("group_tbl._id"), nullable=True)
    #
    # user = relationship("Person", foreign_keys=[_userID], lazy='joined')
    # gp = relationship("Group", foreign_keys=[_group], lazy='joined')

    def __init__(self, title, ticket_datetime, response_type, text):
        self._id = None
        self._title = title
        self._ticket_datetime = ticket_datetime
        self._response_type = response_type
        self._text = text

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def ticket_datetime(self):
        return self._ticket_datetime

    @ticket_datetime.setter
    def ticket_datetime(self, ticket_datetime):
        self._ticket_datetime = ticket_datetime

    @property
    def response_type(self):
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        self._response_type = response_type

    @property
    def text(self):
        return self._text

    @text.setter
    def group(self, text):
        self._text = text
