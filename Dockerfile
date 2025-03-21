FROM python:3.9.6-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements_venv.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
