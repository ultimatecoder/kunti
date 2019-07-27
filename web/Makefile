install:
	pip install pipenv
	pipenv install --dev
lint:
	flake8 kunti
test:
	cd kunti && pipenv run python manage.py test
run: migrate
	cd kunti && pipenv run python manage.py runserver
migrate:
	cd kunti && pipenv run python manage.py migrate
makemigrations:
	cd kunti && pipenv run python manage.py makemigrations
