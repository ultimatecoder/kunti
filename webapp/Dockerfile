FROM python

WORKDIR /usr/src/kunti

COPY kunti .

COPY Pipfile .

COPY Pipfile.lock .

RUN pip install pipenv

RUN pipenv install

EXPOSE 8000

ENV STATIC_ROOT /srv/www/static

COPY scripts/start.sh start.sh

CMD bash start.sh
