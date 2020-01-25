from datetime import datetime
from sqlalchemy import ForeignKey, Sequence, Column, Integer, Float, DateTime, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, index=True)
    name = Column(String)

    measurements = relationship('Measurement', back_populates='users')

class Measurement(Base):
    __tablename__ = 'Measurement'

    id = Column(Integer, Sequence('measurement_id_seq'), primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    date = Column(DateTime, default=datetime.utcnow)
    value = Column(Float)

    users = relationship('User', back_populates='measurements')
