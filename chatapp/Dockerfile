FROM python

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY . /app

RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
EXPOSE 8000

CMD ["manage.py","runserver"]
