FROM python:3.6-alpine

WORKDIR /server

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY *.py ./

EXPOSE 8080

CMD python server.py
