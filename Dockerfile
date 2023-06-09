FROM python:3.10.4-alpine3.15

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN  python3 -m venv .venv
RUN  source .venv/bin/activate

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app"]