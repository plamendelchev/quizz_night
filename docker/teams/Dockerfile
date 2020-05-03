FROM quizz_flask:base

WORKDIR /usr/src/app

COPY . .

CMD ["uwsgi", "--ini", "./app.ini"]
