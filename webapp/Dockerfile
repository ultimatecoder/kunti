FROM python

WORKDIR /usr/src/kunti

COPY Pipfile .

COPY Pipfile.lock .

RUN pip install pipenv

RUN pipenv install

EXPOSE 8000

ENV STATIC_ROOT /srv/www/static

COPY scripts/start.sh start.sh

COPY kunti .

CMD bash start.sh
