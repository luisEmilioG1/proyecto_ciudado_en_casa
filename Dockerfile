FROM python:3.11.4

WORKDIR /app

RUN pip install --upgrade pip==23.1.2

RUN  python3 -m venv .venv 
RUN source .venv/bin/activate

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app"]