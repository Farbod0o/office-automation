from model.da.data_access import Base
from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship


class TicketGroup(Base):
    __tablename__ = "ticket_group"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(30), nullable=False)
    _parent_id = Column("parent_id", Integer, ForeignKey("ticket_group.id"), nullable=True)
    # _child_id = Column("child_id", Integer, ForeignKey("ticket_group_id"), nullable=True)

    parent = relationship("TicketGroup", remote_side=_id)

    def __init__(self, name, parent):
        self._id = None
        self._name = name
        self._parent_id = parent._id if parent else None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        self._parent_id = parent_id
