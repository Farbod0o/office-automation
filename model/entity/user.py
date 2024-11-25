from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.da.data_access import Base
from model.tools.validator import pattern_validator
import hashlib

class User(Base):
    __tablename__ = "user_tbl"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(30), nullable=False, unique=True)
    password = Column("password", String(128), nullable=False)
    email = Column(String(50), unique=True)
    role_id = Column(Integer, ForeignKey("role_tbl.id"), nullable=False)
    person_id = Column(Integer, ForeignKey("person_tbl.id"), nullable=False)

    role = relationship("Role", back_populates="users")
    person = relationship("Person", back_populates="user")

    def __init__(self, user_name, password, email, role_id, person_id):
        self.user_name = user_name
        self.password = password
        self.email = email
        self.role_id = role_id
        self.person_id = person_id

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    @pattern_validator(r'^[A-Za-z0-9_]{3,30}$', "نام کاربری باید شامل حروف، اعداد یا '_' باشد و حداقل 3 و حداکثر 30 کاراکتر داشته باشد.")
    def user_name(self, value):
        self._user_name = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError("رمز عبور باید حداقل 8 کاراکتر داشته باشد.")
        self._password = hashlib.sha256(value.encode('utf-8')).hexdigest()

    @property
    def email(self):
        return self._email

    @email.setter
    @pattern_validator(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', "ایمیل معتبر نیست.")
    def email(self, value):
        self._email = value
