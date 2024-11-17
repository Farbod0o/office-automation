from enum import Enum
from sqlalchemy import Column, String, Integer , relationship
from model.tools.validator import pattern_validator
from model.entity.bace import Bace


class System_User(Bace):
    __tablename__ = "system_users"
    user_code = Column(Integer, primary_key=True , unique=True)
    personal_code = Column(Integer, nullable=False, unique=True, index=True)
    part_code = Column(String(8), nullable=False)
    user_name = Column(String(20), nullable=False, unique=True)
    password = Column(String(32), nullable=False)
    role = Column(String(15), nullable=False)
    status = Column(Enum("Active", "Inactive", name="status_enum"), nullable=False)

    massages = relationship("Massage", back_populates="person")
    person = relationship("Person", back_populates="system_user", uselist=False)


def __init__(self, user_code, pesonal_code, part_code, user_name, password, role, status=True):
    self.user_code = user_code
    self.pesonal_code = pesonal_code
    self.part_code = part_code
    self.user_name = user_name
    self.password = password
    self.role = role
    self.status = status







@property


def user_code(self):
    return self._user_code


@user_code.setter
@pattern_validator(r'^[A-Za-z0-9]{1,10}$',
                   "کد کاربر باید دارای نویسه های الفبایی عددی و حداکثر 10 کاراکتر باشد.")
def user_code(self, value):
    self._user_code = value


@property
def personal_code(self):
    return self._personal_code


@personal_code.setter
@pattern_validator(r'^[A-Za-z0-9]{1,12}$',
                   "کد شخصی باید دارای نویسه های الفبایی عددی و حداکثر 12 کاراکتر باشد.")
def personal_code(self, value):
    self._personal_code = value


@property
def part_code(self):
    return self._part_code


@part_code.setter
@pattern_validator(r'^[A-Za-z0-9]{1,8}$',
                   "کد قسمت باید دارای نویسه های الفبایی عددی و حداکثر 8 کاراکتر باشد.")
def part_code(self, value):
    self._part_code = value


@property
def user_name(self):
    return self._user_name


@user_name.setter
@pattern_validator(r'^[A-Za-z0-9_]{1,20}$',
                   "نام کاربری باید دارای نویسه های الفبایی عددی و حداکثر 20 کاراکتر باشد.")
def user_name(self, value):
    self._user_name = value


@property
def password(self):
    return self._password


@password.setter
@pattern_validator(r'^[\S]{8,32}$', "رمز عبور باید 8 تا 32 کاراکتر باشد و نباید دارای فاصله باشد.")
def password(self, value):
    self._password = value


@property
def role(self):
    return self._role


@role.setter
@pattern_validator(r'^[A-Za-z]{1,15}$', "نقش باید دارای حروف الفبا و حداکثر 15 کاراکتر باشد.")
def role(self, value):
    self._role = value


@property
def status(self):
    return self._status


@status.setter
@pattern_validator(r'^(Active|Inactive|فعال|غیرفعال)$', "وضعیت باید فعال یا غیرفعال باشد.")
def status(self, value):
    self._status = value
