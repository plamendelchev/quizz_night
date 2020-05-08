FROM quizz_uwsgi:base

WORKDIR /usr/src/app
COPY . .

CMD ["uwsgi", "--ini", "./app.ini"]
