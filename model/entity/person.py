from sqlalchemy import Integer, Column, String
from model.da.data_access import Base
from model.tools.validator import pattern_validator


class Person(Base):
    __tablename__ = "person_tbl"
    _id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    _sex = Column(String(30), nullable=False)
    _name = Column(String(30), nullable=False)
    _last_name = Column(String(30), nullable=False)
    _national_code = Column(Integer, nullable=False, unique=True, index=True)

    def __init__(self, sex, name, last_name, national_code):
        self.id = None
        self.sex = sex
        self.name = name
        self.last_name = last_name
        self.national_code = national_code

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
    @pattern_validator(r'^[A-Za-zآ-ی]{1,16}$',
                       "نام فقط باید دارای حروف الفبا (لاتین یا فارسی) و حداکثر 16 کاراکتر باشد.")
    def name(self, value):
        self._name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    @pattern_validator(r'^[A-Za-zآ-ی]{1,16}$',
                       "نام خانوادگی فقط باید دارای حروف الفبا و حداکثر 16 کاراکتر باشد.")
    def last_name(self, value):
        self._last_name = value

    @property
    def sex(self):
        return self._sex

    @sex.setter
    @pattern_validator(r'^[A-Za-z]{1,4}$',
                       "جنسیت فقط باید دارای حروف الفبا و حداکثر 4 کاراکتر باشد.")
    def sex(self, value):
        self._sex = value

    @property
    def national_code(self):
        return self._national_code

    @national_code.setter
    @pattern_validator(r'^\d{10}$', "کد ملی باید دقیقاً شامل 10 رقم عددی باشد.")
    def national_code(self, value):
        self._national_code = value
