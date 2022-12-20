FROM python:3.9.7

COPY . .

RUN pip install -r requirements.txt

RUN chmod a+x run.sh

WORKDIR /app

RUN chmod a+x run.sh

CMD ["./run.sh"]
