from sqlalchemy import Column, Integer, String, DateTime, Date
from model.entity.base import Base
from model.tools.validator import pattern_validator


class Property(Base):
    __tablename__ = "property_tbl"
    _property_code = Column("property_code", Integer, primary_key=True, nullable=False, unique=True)
    _group_code = Column("group_code", Integer, nullable=False, unique=True)
    _property_name = Column("property_name", String(30), nullable=False)
    _property_description = Column("property_description", String(200), nullable=False)
    _label_code = Column("label_code", Integer, nullable=False, unique=True)
    _count = Column("count", Integer, nullable=False)
    _property_price = Column("property_price", Integer, nullable=False)
    _delivery_date = Column("delivery_date", DateTime, nullable=False)
    _section_code = Column("section_code", Integer, nullable=False)
    _personal_code_delivery = Column("personal_code_delivery", Integer, nullable=False)
    _image = Column("image", String(30), nullable=False)
    _status = Column("status", String(100), nullable=False)

    def __init__(self, property_code, group_code, property_name, property_description, label_code,
                 count, property_price, delivery_date, section_code, personal_code_delivery
                 , image, status):
        self._property_code = property_code
        self._group_code = group_code
        self._property_name = property_name
        self._property_description = property_description
        self._label_code = label_code
        self._count = count
        self._property_price = property_price
        self._delivery_date = delivery_date
        self._section_code = section_code
        self._personal_code_delivery = personal_code_delivery
        self._image = image
        self._status = status

    @property
    def property_code(self):
        return self._property_code

    @property_code.setter
    @pattern_validator(r"^[0-9]{2,30}$", " معتبر نیست!")
    def property_code(self, property_code):
        self._property_code = property_code

    @property
    def group_code(self):
        return self._group_code

    @group_code.setter
    @pattern_validator(r"^[0-9]{2,30}$", " معتبر نیست!")
    def group_code(self, group_code):
        self._group_code = group_code

    @property
    def property_name(self):
        return self._property_name

    @property_name.setter
    @pattern_validator(r"^[A-Za-z]{2,30}$", " معتبر نیست!")
    def property_name(self, property_name):
        self._property_name = property_name

    @property
    def property_description(self):
        return self._property_description

    @property_description.setter
    @pattern_validator(r"^[A-Za-z]{2,200}$", " معتبر نیست!")
    def description(self, property_description):
        self._property_description = property_description

    @property
    def label_code(self):
        return self._label_code

    @label_code.setter
    @pattern_validator(r"^[0-9]{2,30}$", " معتبر نیست!")
    def label_code(self, property_code):
        self._label_code = property_code

    @property
    def count(self):
        return self._count

    @count.setter
    @pattern_validator(r"^[0-9]{2,30}$", " معتبر نیست!")
    def count(self, count):
        self._count = count

    @property
    def property_price(self):
        return self._property_price

    @property_price.setter
    @pattern_validator(r"^[0-9]{2,30}$", " معتبر نیست!")
    def property_price(self, property_price):
        self._property_price = property_price

    @property
    def delivery_date(self):
        return self._delivery_date

    @delivery_date.setter
    @pattern_validator(r"^[0-9]{2,10}$", " معتبر نیست!")
    def delivery_date(self, delivery_date):
        self._delivery_date = delivery_date

    @property
    def section_code(self):
        return self._section_code

    @section_code.setter
    @pattern_validator(r"^[0-9]{2,30}$", " معتبر نیست!")
    def section_code(self, section_code):
        self._section_code = section_code

    @property
    def personal_code_delivery(self):
        return self._personal_code_delivery

    @personal_code_delivery.setter
    @pattern_validator(r"^[0-9]{2,30}$", " معتبر نیست!")
    def personal_code_delivery(self, personal_code_delivery):
        self._personal_code_delivery = personal_code_delivery

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image

    @property
    def status(self):
        return self._status

    @status.setter
    @pattern_validator(r"^[a-zA-Z]$", " معتبر نیست!")
    def status(self, status):
        self._status = status


