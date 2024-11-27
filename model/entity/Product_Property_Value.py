from sqlalchemy import Column, Integer, String, relationship
from model.entity.base import Base
from model.tools.validator import pattern_validator


class Product_Property_Value(Base):
    __tablename__ = "Product_Property_Value_tbl"
    _id = Column("id", primary_key=True, autoincrement=True, nullable=False)
    _color = Column("color", String(30), nullable=False)
    _size = Column("size", Integer, nullable=False)
    _weight = Column("weight", Integer, nullable=False)
    _description = Column("description", String(200), nullable=False)
    _material = Column("material", String(30), nullable=False)

    def __init__(self, id, color, size, weight, description, material):
        self._id = None
        self._color = color
        self._size = size
        self._weight = weight
        self._description = description
        self._material = material

    @property
    def id(self):
        return self._id

    @id.setter
    @pattern_validator("^[0-9]$", "آیدی معتبر نیست!")
    def id(self, id):
        self._id = id

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if isinstance(color, str):
            self._color = color
        else:
            raise ValueError("رنگ معتبر نیست")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size

        else:
            raise ValueError("سایز معتبر نیست")

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if isinstance(weight, int):
            self._weight = weight

        else:
            raise ValueError("وزن معتبر نیست")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self._description = description
        else:
            raise ValueError("توضیحات معتبر نیست")

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, material):
        if isinstance(material, str):
            self._material = material

        else:
            raise ValueError("متریال معتبر نیست")
