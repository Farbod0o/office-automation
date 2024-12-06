from sqlalchemy import Column, Integer, String, ForeignKey, Table
from model.da.data_access import Base



user_permission_table = Table(
    'user_permission_tbl', Base.metadata,
    Column('user_id', Integer, ForeignKey('user_tbl.id')),
    Column('permission_id', Integer, ForeignKey('permission_tbl.id'))
)