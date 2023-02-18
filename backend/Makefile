.DEFAULT_GOAL := help

help: ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"

requirementslocal: ## install local environment requirements
	pip install -r requirements/requirementslocal.txt 

requirementsprod: ## install production environment requirements
	pip install -r requirements/requirementsprod.txt 

makemigrationslocal: ## makemigrations
	python manage.py makemigrations

migratelocal: ## migrate
	python manage.py migrate

runlocal: ## runserver django project port 8000
	python manage.py runserver 0.0.0.0:8000