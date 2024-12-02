from sqlalchemy import Integer, Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from model.da.data_access import Base
from model.tools.validator import pattern_validator


class Massage(Base):
    __tablename__ = 'massage_tbl'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _text = Column("text", String(250), nullable=False)
    _date_time = Column(DateTime)
    _title = Column("title", String(250), nullable=False)
    _membername = Column("membername", String(30), nullable=False)

    # system_user = relationship("System_User", back_populates="massages")
    # person = relationship("Person", back_populates="massages")
    # property = relationship("Property", back_populates="massages")

    def __init__(self, text, date_time, title, membername):
        self._id = None
        self.text = text
        self.date_time = date_time
        self.title = title
        self.membername = membername

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    @pattern_validator(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$",
                       "تاریخ و ساعت باید به این الگو باشد .'YYYY-MM-DD HH:MM:SS'.")
    def date_time(self, date_time):
        self._date_time = date_time

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
