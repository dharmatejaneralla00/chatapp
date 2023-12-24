FROM python

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
EXPOSE 9000

CMD ["manage.py","runserver","0.0.0.0:9000" ]
