from sqlalchemy import Column, Integer, String, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from model.tools.validator import pattern_validator
from model.da.data_access import Base


class Letter(Base):
    __tablename__ = "letter_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String(30), nullable=False)
    _content = Column("content", String(30), nullable=False)
    _sender = Column("sender", String(30), nullable=False)
    _receiver = Column("receiver", String(30), nullable=False)
    _created_at = Column("created_at", DateTime, nullable=False)
    # _reference_id = Column("reference_id", Integer, ForeignKey("reference.id"), nullable=False)


    # reference = relationship("reference", back_populates="letters_tbl")

    def __init__(self, title, content, sender, receiver, created_at, reference_id):
        self.title = title
        self.content = content
        self.sender = sender
        self.receiver = receiver
        self.created_at = created_at
        self.reference_id = reference_id

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    @pattern_validator(r'^[A-Za-zآ-ی\s]{1,100}$', "عنوان باید حداکثر 100 کاراکتر باشد و شامل حروف فارسی یا انگلیسی.")
    def title(self, value):
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def sender(self):
        return self._sender

    @sender.setter
    @pattern_validator(r'^[A-Za-zآ-ی\s]{1,50}$', "فرستنده باید شامل حروف فارسی یا انگلیسی باشد و حداکثر 50 کاراکتر.")
    def sender(self, value):
        self._sender = value

    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    @pattern_validator(r'^[A-Za-zآ-ی\s]{1,50}$', "گیرنده باید شامل حروف فارسی یا انگلیسی باشد و حداکثر 50 کاراکتر.")
    def receiver(self, value):
        self._receiver = value

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        self._created_at = value

    @property
    def reference_id(self):
        return self._reference_id

    @reference_id.setter
    def reference_id(self, value):
        self._reference_id = value
