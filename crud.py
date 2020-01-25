from sqlalchemy.orm import Session
import models


def create_measurement(db: Session, user_id: int, value: float):
    measurement = models.Measurement(user_id=user_id, value=value)
    db.add(measurement)
    db.commit()
    db.refresh(measurement)
    return measurement


def get_weight(db: Session, user_id: int) -> float:
    return db.query(models.Measurement).filter(models.Measurement.user_id == user_id).first()
