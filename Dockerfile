FROM python:3.8
EXPOSE 8000

COPY . /code
WORKDIR /code

RUN pip install -r requirements.txt

CMD uvicorn --host 0.0.0.0 --port 80 main:app
