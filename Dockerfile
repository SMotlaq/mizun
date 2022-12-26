FROM python:3.9.7

RUN apt update && apt-get install -y bmon pv netcat

COPY . .

RUN pip install -r requirements.txt

WORKDIR /app

RUN chmod 777 get_stat.sh uploader.sh

CMD ["python","main.py"]
