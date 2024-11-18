from sqlalchemy import Column, Integer, String
from model.tools.validator import pattern_validator
from model.entity.base import Base


class ProductGroup(Base):
    __tablename__ = "product_group_tbl"
    _group_code = Column("group_code", Integer, nullable=False,primary_key=True)
    _product_group_name = Column("product_group_name", String(30), nullable=False)
    _group_code_up = Column("_group_code_up", Integer, nullable=False)
    _description = Column("_description", String(200), nullable=False)

    def __init__(self, group_code, product_group_name, group_code_up, description):
        self._group_code = group_code
        self._product_group_name = product_group_name
        self._group_code_up = group_code_up
        self._description = description

    def __repr__(self):
        return f"{self.__dict__}"

    @property
    def group_code(self):
        return self._group_code

    @group_code.setter
    @pattern_validator(r"^[0-9]{2,30}$", " کد گروه معتبر نیست !")
    def group_code(self, group_code):
        self._group_code = group_code

    @property
    def product_group_name(self):
        return self._product_group_name

    @product_group_name.setter
    @pattern_validator(r"^[A-Za-z]{2,30}$", "نام گروه کالا معتبر نیست!")
    def product_group_name(self, product_group_name):
        self._product_group_name = product_group_name

    @property
    def group_code_up(self):
        return self._group_code

    @group_code_up.setter
    @pattern_validator(r"^[0-9]{2,30}$", " کد گروه بالا دستی معتبر نیست!")
    def group_code_up(self, group_code_up):
        self._group_code_up = group_code_up

    @property
    def description(self):
        return self._description

    @product_group_name.setter
    @pattern_validator(r"^[A-Za-z]{2,200}$", " توضیحات معتبر نیست!")
    def description(self, description):
        self._description = description




