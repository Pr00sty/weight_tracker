from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED
from models import Measurement


def create_measurement(db: Session, user_id: int, value: float) -> Measurement:
    if user_id <= 0:
        raise ValueError("id cannot be <= 0")
    if value <= 0:
        raise ValueError("value cannot be <= 0")
    measurement = Measurement(user_id=user_id, value=value)
    db.add(measurement)
    db.commit()
    db.refresh(measurement)
    return measurement


def get_weight(db: Session, user_id: int) -> float:
    return db.query(Measurement).filter(Measurement.user_id == user_id).first()
