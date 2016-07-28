
from zingkd.models.meta import Base

from sqlalchemy import Column, func
from sqlalchemy.types import Unicode, Integer, DateTime, Boolean, UnicodeText
from sqlalchemy.orm import relationship, backref


class Note(Base):
    __tablename__ = 'notes'
    __table_args__ = {'schema': 'zingk'}

    note_id = Column(Integer, primary_key=True)

    title = Column(Unicode(255), nullable=False)
    created = Column(DateTime, nullable=False, server_default=func.now())
    modified = Column(DateTime, nullable=False, server_default=func.now())
    colour = Column(Unicode(6), nullable=False, server_default='CCCCCC')
    #archived = Column(Boolean, nullable=False, server_default=False)
    content = Column(UnicodeText, nullable=False)
