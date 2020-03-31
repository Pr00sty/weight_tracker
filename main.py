from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response
from starlette.status import HTTP_201_CREATED, HTTP_409_CONFLICT

import crud
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.put('/add_measurement/user_id={user_id}&weight={weight}')
async def create_measurement(user_id: int, weight: float, response: Response, db: Session = Depends(get_db)):
    try:
        response.status_code = HTTP_201_CREATED
        return crud.create_measurement(db=db, user_id=user_id, value=weight)
    except ValueError:
        response.status_code = HTTP_409_CONFLICT
    except TypeError:
        response.status_code = HTTP_409_CONFLICT


@app.get("/get_weight/{user_id}")
async def get_weight(user_id: int, db: Session = Depends(get_db)) -> float:
    return crud.get_weight(db=db, user_id=user_id)
