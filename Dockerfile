FROM python

WORKDIR /usr/src/kunti

COPY kunti .

COPY Makefile .

COPY Pipfile .

COPY Pipfile.lock .

RUN make install

EXPOSE 8000

CMD ["pipenv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "--chdir", "kunti", "kunti.wsgi:application"]
