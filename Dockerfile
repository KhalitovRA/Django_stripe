FROM python

WORKDIR /django_stripe

RUN pip install django

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.8000"]