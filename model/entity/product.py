from sqlalchemy import Column, Integer, String
from model.entity.base import Base
from model.tools.validator import pattern_validator


class Product(Base):
    __tablename__ = "product_tbl"
    _id = Column("id", Integer, primary_key=True, nullable=False, autoincrement=True)
    _name = Column("name", String(30), nullable=False)
    _price = Column("price", Integer, nullable=False)
    _code = Column("code", Integer, nullable=False)
    _description = Column("description", String(200), nullable=False)
    _image = Column("image", String(30), nullable=False)

    def __init__(self, name, price, code, description, image):
        self._id = None
        self._name = name
        self._price = price
        self._code = code
        self._description = description
        self._image = image

    @property
    def id(self):
        return self._id

    @id.setter
    @pattern_validator("^[0-9]{2,03}$", "آیدی معتبر نیست!")
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("نام معتبر نیست")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, int):
            self._price = price

        else:
            raise ValueError("ارزش معتبر نیست")

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        if isinstance(code, int):
            self._code = code
        else:
            raise ValueError("کد معتبر نیست")

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
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image
