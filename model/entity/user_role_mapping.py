from sqlalchemy import Column, Integer, String, ForeignKey, Table

from model.da.data_access import Base

user_role_table = Table(
    "user_role_tbl", Base.metadata,
    Column('user_id', Integer, ForeignKey('user_tbl.id')),
    Column('role_id', Integer, ForeignKey('role_tbl.id'))
)


