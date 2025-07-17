FROM python:3-slim

WORKDIR /app 

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt 

COPY .  .

EXPOSE 5000

ENV FLASK_APP=main.py

ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
