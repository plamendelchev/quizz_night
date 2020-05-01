FROM quizz_flask/base

WORKDIR /usr/src/app

COPY app.py .
COPY app.ini .
COPY wsgi.py .

CMD ["uwsgi", "--ini", "app.ini"]
