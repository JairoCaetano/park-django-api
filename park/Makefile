all:
	@make migrations
	@make migrate
	@make run

run:
	@python3 manage.py runserver

migrations:
	@python3 manage.py makemigrations

migrate:
	@python3 manage.py migrate

psh:
	@python manage.py shell

.PHONY:run migrations migrate
