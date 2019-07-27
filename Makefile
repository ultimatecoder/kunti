install:
	pip install pipenv
	pipenv install --dev
lint:
	flake8 --exclude=migrations kunti
test:
	cd kunti && pipenv run python manage.py test
run: migrate
	cd kunti && pipenv run python manage.py runserver
migrate:
	cd kunti && pipenv run python manage.py migrate
migrations:
	cd kunti && pipenv run python manage.py makemigrations
