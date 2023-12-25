FROM python

WORKDIR /app
COPY . /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
EXPOSE 8000

CMD ["manage.py","runserver","0.0.0.0:8000]
