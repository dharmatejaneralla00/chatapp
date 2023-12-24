FROM python

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY . /app

RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
EXPOSE 9000

CMD ["manage.py","runserver","0.0.0.0:9000" ]
