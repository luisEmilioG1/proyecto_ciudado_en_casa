FROM python:3.11.4-slim-buster
WORKDIR /app


RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libc-dev \
        libpq-dev \
        libffi-dev \
        mariadb-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip==23.1.2

#RUN  python3 -m venv .venv 
#RUN source .venv/bin/activate

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app"]