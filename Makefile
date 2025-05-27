.PHONY: runprod rmprod db api ui

run:
	docker-compose up

rm:
	docker-compose rm --force

db:
	docker run -d --name pokedex-db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -v pokedex_postgres_data:/var/lib/postgresql/data postgres:15

be:
	fastapi dev --host "0.0.0.0" --port 8000 --reload src/vce/app.py
