FROM python:3.8-slim-buster

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./app/app.py /app

COPY ./src /app/src

EXPOSE 3000

CMD ["python", "app.py" ]