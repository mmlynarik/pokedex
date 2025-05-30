.PHONY: runprod rmprod db api ui

run:
	docker-compose up

container:
	docker run --name pokedex --rm -p 8000:8000 pokedex

rm:
	docker-compose rm --force

db:
	docker run -d --name pokedex-db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -v pokedex_postgres_data:/var/lib/postgresql/data postgres:15

superuser:
	python src/djangoproject/manage.py createsuperuser

django:
	python src/djangoproject/manage.py makemigrations && \
	python src/djangoproject/manage.py migrate && \
	python src/djangoproject/manage.py runserver
