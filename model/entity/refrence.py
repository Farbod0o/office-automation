from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean
from sqlalchemy.orm import relationship
from model.da.data_access import Base
from model.tools.validator import pattern_validator

class Reference(Base):
    __tablename__ = "reference_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _reference_num = Column("reference_num", String(50), nullable=False, unique=True)
    _type = Column("type", Enum("official","informal","urgent"), nullable=False)
    _security = Column("security", Boolean, default=False)
    _priority = Column("priority", String(20))
    _referral_date_time = Column("referral_date_time", DateTime, nullable=False)
    _expire_date_time = Column("expire_date_time", DateTime, nullable=True)
    _paraph = Column("paraph", String(255))
    _status = Column("status", Enum("pending","approved","rejectedd"), nullable=False)
    _description = Column("description", String(2000), nullable=True)
    _confirmation = Column("confirmation", String(50))
    _receive_send = Column("receive_send", Enum("recive","send"), nullable=False)
    _access_level = Column("access_level", String(50))
    # letters = relationship("letter", back_populates="reference_tbl")


    def __init__(self, reference_num, type_, security, referral_date_time, status, receive_send, priority=None,
                 expire_date_time=None, paraph=None, description=None, confirmation=None, access_level=None):
        self.reference_num = reference_num
        self.type = type_
        self.security = security
        self.referral_date_time = referral_date_time
        self.status = status
        self.receive_send = receive_send
        self.priority = priority
        self.expire_date_time = expire_date_time
        self.paraph = paraph
        self.description = description
        self.confirmation = confirmation
        self.access_level = access_level

    @property
    def reference_num(self):
        return self._reference_num

    @reference_num.setter
    @pattern_validator(r'^[A-Za-z0-9\-]+$', "شماره مرجع باید فقط شامل حروف، اعداد و خط تیره باشد.")
    def reference_num(self, value):
        self._reference_num = value

    @property
    def paraph(self):
        return self._paraph

    @paraph.setter
    @pattern_validator(r'^.{0,255}$', "پاراگراف باید حداکثر 255 کاراکتر باشد.")
    def paraph(self, value):
        self._paraph = value


