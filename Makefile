# Develop
include .env

ifeq ($(USE_DOCKER), True)
%: # catch all commands and run into docker container
	docker-compose run --rm backend bash -c 'make -e USE_DOCKER=False $@'

bash:
	docker-compose run --rm backend bash
else
# local commands
check:
	black --check .
	flake8
	isort --check-only --recursive
	mypy .

fix:
	pre-commit run --all-files

collectstatic:
	python manage.py collectstatic --clear --noinput


dev:
	pip install -q pip~=20.0.1 pip-tools~=4.4.0
	pip-sync requirements/dev.txt

migrate:
	python manage.py migrate --noinput

migrations:
	python manage.py makemigrations --no-header

pip:
	pip install -q pip~=20.0.1 pip-tools~=4.4.0
	pip-compile $(p) requirements/common.ini > requirements/common.txt
	pip-compile $(p) requirements/dev.ini > requirements/dev.txt
	pip-compile $(p) requirements/prod.ini > requirements/prod.txt
	pip-compile $(p) requirements/tests.ini > requirements/tests.txt
	pip-compile $(p) requirements/local.ini > requirements/local.txt

tox:
	tox -e coverage,reporthtml,report

test:
	coverage run manage.py test --settings=backend.settings --noinput; coverage report; coverage html -d htmlcov

dbshell:
	python manage.py shell

shell:
	python manage.py shell

graph_models:
	python manage.py graph_models -o graph_models.svg

createsuperuser:
	python manage.py createsuperuser

importdata:
	python manage.py import_data

endif

dockerprecommit:
	pre-commit install --config .pre-commit-config.docker.yaml
