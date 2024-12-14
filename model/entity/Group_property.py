from sqlalchemy import Column, Integer, String,ForeignKey
from model.entity.base import Base
from model.tools.validator import pattern_validator


class Group_property(Base):
    __tablename__ = "group_property_tbl"
    _id = Column("id", Integer, primary_key=True, nullable=False,autoincrement=True)
    _title = Column("_title", String(30), nullable=False)

    def __init__(self,title):
        self._id = None
        self._title = title

    @property
    def id(self):
        return self._id

    @id.setter
    @pattern_validator("^[0-9]$", "آیدی معتبر نیست!")
    def id(self, id):
        self._id = id

    @property
    def title(self):
        return self._title


    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise ValueError("عنوان معتبر نیست")
