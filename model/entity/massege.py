from sqlalchemy import Integer, Column, String, ForeignKey, DateTime , relationship
from model.da.data_access import Base
from model.tools.validator import pattern_validator

class Massage(Base):
    __tablename__ = 'massage_tbl'
    text =Column(String, primary_key=True)
    date_time = Column(DateTime)
    user_id = Column(Integer, ForeignKey('system_users.user_code'))


    system_user = relationship("System_User", back_populates="massages")
    person = relationship("Person", back_populates="massages")
    property = relationship("Property", back_populates="massages")




    def __init__(self, text, date_time, user_id):
        self.text = text
        self.date_time = date_time
        self.user_id = user_id

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    @pattern_validator(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$',
                       "تاریخ و ساعت باید به این الگو باشد . 'YYYY-MM-DD HH:MM:SS'.")
    def date_time(self, value):
        self._date_time = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    @pattern_validator(r'^[0-9]+$', "ایدی کاربر باید عدد باشد .")
    def user_id(self, value):
        self._user_id = value

