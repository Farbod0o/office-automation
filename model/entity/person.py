from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.da.data_access import Base
from model.tools.validator import pattern_validator

class Person(Base):
    __tablename__ = "person_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column(String(30), nullable=False)
    _family = Column(String(30), nullable=False)
    _national_id = Column(String(10), nullable=False, unique=True)
    _birth_date = Column(String(10),nullable=False)
    _phone = Column(String(15),nullable=False)
    _address = Column(String(255),nullable=False)
    _post_code = Column(String(10),nullable=False)

    user = relationship("User", back_populates="person", uselist=False)

    def __init__(self, name, family, national_id, birth_date=None, phone=None, address=None, post_code=None):
        self.name = name
        self.family = family
        self.national_id = national_id
        self.birth_date = birth_date
        self.phone = phone
        self.address = address
        self.post_code = post_code

    @property
    def name(self):
        return self._name

    @name.setter
    @pattern_validator(r'^[A-Za-zآ-ی]{1,30}$', "نام باید فقط شامل حروف الفبا و حداکثر 30 کاراکتر باشد.")
    def name(self, value):
        self._name = value

    @property
    def family(self):
        return self._family

    @family.setter
    @pattern_validator(r'^[A-Za-zآ-ی]{1,30}$', "نام خانوادگی باید فقط شامل حروف الفبا و حداکثر 30 کاراکتر باشد.")
    def family(self, value):
        self._family = value

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    @pattern_validator(r'^\d{10}$', "کد ملی باید دقیقاً شامل 10 رقم عددی باشد.")
    def national_id(self, value):
        self._national_id = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    @pattern_validator(r'^\d{8,15}$', "شماره تلفن باید شامل حداقل 8 و حداکثر 15 رقم باشد.")
    def phone(self, value):
        self._phone = value

    @property
    def post_code(self):
        return self._post_code

    @post_code.setter
    @pattern_validator(r'^\d{10}$', "کد پستی باید دقیقاً شامل 10 رقم باشد.")
    def post_code(self, value):
        self._post_code = value

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
