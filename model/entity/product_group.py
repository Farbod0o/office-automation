from sqlalchemy import Column, Integer, String, ForeignKey
from model.tools.validator import pattern_validator
from model.entity.base import Base
from sqlalchemy.orm import relationship


class ProductGroup(Base):
    __tablename__ = "product_group_tbl"
    _id = Column("id", Integer, primary_key=True, nullable=False, autoincrement=True)
    _name = Column("name", String(30), nullable=False)
    _parent_id = Column(Integer, ForeignKey("product_group.id"))
    _child_id = Column(Integer, ForeignKey("product_group.id"))

    product_gp = relationship("ProductGroup", back_populates="ProductGroup")

    def __init__(self, name):
        self._id = None
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    @pattern_validator("^[0-9]$", "آیدی معتبر نیست")
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    @pattern_validator("^[a-zA-Z]{2,30}$", "نام معتبر نیست")
    def name(self, name):
        self._name = name
