FROM python

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]

CMD ["python","manage.py","runserver","0.0.0.0:9000" ]
