from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine

import crud
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.put('/add_measurement/{id}')
async def create_measurement(user_id: int, value: float, db: Session = Depends(get_db)):
    return crud.create_measurement(db=db, user_id=user_id, value=value)

@app.get("/")
async def get_weight(user_id: int, db: Session = Depends(get_db)) -> float:
    return crud.get_weight(db=db, user_id=user_id)
