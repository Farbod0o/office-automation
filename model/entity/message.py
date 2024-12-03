from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from model.da.data_access import Base


class Message(Base):
    __tablename__ = "message_tbl"

    _id = Column(Integer, primary_key=True, autoincrement=True)
    _title = Column(String(100), nullable=False)
    _datetime = Column(DateTime, nullable=False)
    _membername = Column(String(50), nullable=False)
    _text = Column(String(500), nullable=False)

    user_id = Column(Integer, ForeignKey("user_tbl.id"), nullable=False)
    ticket_id = Column(Integer, ForeignKey("ticket_tbl.id"), nullable=False)

    user = relationship("User", back_populates="messages")
    ticket = relationship("Ticket", back_populates="messages")

    def __init__(self, title, datetime, membername, text, user_id, ticket_id):
        self.title = title
        self.datetime = datetime
        self.membername = membername
        self.text = text
        self.user_id = user_id
        self.ticket_id = ticket_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def datetime(self):
        return self._datetime

    @datetime.setter
    def datetime(self, value):
        self._datetime = value

    @property
    def membername(self):
        return self._membername

    @membername.setter
    def membername(self, value):
        self._membername = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
