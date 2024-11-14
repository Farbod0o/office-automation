from enum import Enum

from sqlalchemy import Column, String, Integer

from Bace.Bace import Bace
from validator import pattern_validator


class System_User(Bace):
    __tablename__ = "system_users"
    user_code = Column(Integer, primary_key=True , unique=True)
    personal_code = Column(Integer, nullable=False, unique=True, index=True)
    part_code = Column(String(8), nullable=False)
    user_name = Column(String(20), nullable=False, unique=True)
    password = Column(String(32), nullable=False)
    role = Column(String(15), nullable=False)
    status = Column(Enum("Active", "Inactive", name="status_enum"), nullable=False)


def __init__(self, user_code, pesonal_code, part_code, user_name, password, role, status=True):
    self.user_code = user_code
    self.pesonal_code = pesonal_code
    self.part_code = part_code
    self.user_name = user_name
    self.password = password
    self.role = role
    self.status = status





    # Getter and setter for 'user_code'


@property


def user_code(self):
    return self._user_code


@user_code.setter
@pattern_validator(r'^[A-Za-z0-9]{1,10}$',
                   "User code must contain alphanumeric characters and be up to 10 characters long.")
def user_code(self, value):
    self._user_code = value


# Getter and setter for 'personal_code'
@property
def personal_code(self):
    return self._personal_code


@personal_code.setter
@pattern_validator(r'^[A-Za-z0-9]{1,12}$',
                   "Personal code must contain alphanumeric characters and be up to 12 characters long.")
def personal_code(self, value):
    self._personal_code = value


# Getter and setter for 'part_code'
@property
def part_code(self):
    return self._part_code


@part_code.setter
@pattern_validator(r'^[A-Za-z0-9]{1,8}$',
                   "Part code must contain alphanumeric characters and be up to 8 characters long.")
def part_code(self, value):
    self._part_code = value


# Getter and setter for 'user_name'
@property
def user_name(self):
    return self._user_name


@user_name.setter
@pattern_validator(r'^[A-Za-z0-9_]{1,20}$',
                   "Username must contain alphanumeric characters, underscores, and be up to 20 characters long.")
def user_name(self, value):
    self._user_name = value


# Getter and setter for 'password'
@property
def password(self):
    return self._password


@password.setter
@pattern_validator(r'^[\S]{8,32}$', "Password must be 8 to 32 characters long and cannot contain spaces.")
def password(self, value):
    self._password = value


# Getter and setter for 'role'
@property
def role(self):
    return self._role


@role.setter
@pattern_validator(r'^[A-Za-z]{1,15}$', "Role must contain alphabetic characters and be up to 15 characters long.")
def role(self, value):
    self._role = value


# Getter and setter for 'status'
@property
def status(self):
    return self._status


@status.setter
@pattern_validator(r'^(Active|Inactive)$', "Status must be either 'Active' or 'Inactive'.")
def status(self, value):
    self._status = value
