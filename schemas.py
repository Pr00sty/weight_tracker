from datetime import datetime
from pydantic import BaseModel

class MeasurementBase(BaseModel):
    user_id: int
    value: float

class MeasureCreate(MeasurementBase):
    pass

class Measurement(MeasurementBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
