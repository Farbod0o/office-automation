from sqlalchemy import Column, Integer, String
from model.da.data_access import Base
from model.tools.validator import pattern_validator

class Permission(Base):
    tablename = "permission_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column(String(50), nullable=False, unique=True)

    def init(self, name):
        self.name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        raise AttributeError("ID به صورت خودکار مقداردهی می‌شود و قابل تغییر نیست.")

    @property
    def name(self):
        return self._name

    @name.setter
    @pattern_validator(r'^[A-Za-zآ-ی\s]{1,50}$', "نام دسترسی فقط باید شامل حروف الفبا و حداکثر 50 کاراکتر باشد.")
    def name(self, value):
        self._name = value