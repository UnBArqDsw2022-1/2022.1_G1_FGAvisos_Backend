FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir app/

WORKDIR /app/

ADD . . 

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]