# Dockerfile in testing state

FROM python:3.8

RUN python -m pip install --upgrade pip

WORKDIR /service

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload"]
