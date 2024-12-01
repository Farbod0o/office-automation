from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.da.data_access import Base
from model.tools.validator import pattern_validator

class Role(Base):
    __tablename__ = "role_tbl"

    id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(50), nullable=False, unique=True)

    # users = relationship("User", secondary="user_role_tbl", back_populates="roles")

    def __init__(self, role_name):
        self.id = None
        self.role_name = role_name

    @property
    def role_name(self):
        return self._role_name

    @role_name.setter
    @pattern_validator(r'^[A-Za-zآ-ی\s]{1,50}$', "نام نقش فقط باید شامل حروف الفبا و حداکثر 50 کاراکتر باشد.")
    def role_name(self, value):
        self._role_name = value
