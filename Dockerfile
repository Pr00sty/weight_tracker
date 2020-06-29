FROM python:3.8-slim

RUN python -m pip install fastapi uvicorn sqlalchemy

EXPOSE 80

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
