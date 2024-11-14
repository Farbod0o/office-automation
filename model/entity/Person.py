from sqlalchemy import Integer, Column, String

from Bace.Bace import Bace
from validator import pattern_validator


class Person(Bace):
    __tablename__ = "Person"
    person_code = Column(Integer, nullable=False, unique=True, index=True)
    sex = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    national_code = Column(Integer, nullable=False, unique=True, index=True)


def __init__(self, person_code, sex, name, last_name, national_code):
    self.person_code = person_code
    self.sex = sex
    self.name = name
    self.last_name = last_name
    self.national_code = national_code

    # Getter and setter for 'name'
    @property
    def name(self):
        return self._name

    @name.setter
    @pattern_validator(r'^[A-Za-z]{1,16}$',
                       "Name must only contain alphabetic characters and be up to 16 characters long.")
    def name(self, value):
        self._name = value

    # Getter and setter for 'last_name'
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    @pattern_validator(r'^[A-Za-z]{1,16}$',
                       "Last name must only contain alphabetic characters and be up to 16 characters long.")
    def last_name(self, value):
        self._last_name = value

    # Getter and setter for 'sex'
    @property
    def sex(self):
        return self._sex

    @sex.setter
    @pattern_validator(r'^[A-Za-z]{1,4}$',
                       "Sex must only contain alphabetic characters and be up to 4 characters long.")
    def sex(self, value):
        self._sex = value

    # Getter and setter for 'national_code'
    @property
    def national_code(self):
        return self._national_code

    @national_code.setter
    @pattern_validator(r'^\d{10}$', "National code must only contain exactly 10 numeric digits.")
    def national_code(self, value):
        self._national_code = value
