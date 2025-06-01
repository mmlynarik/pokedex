# Pokedex API Django Project

## Project Features
- Automatic PokeAPI data fetch during first app start
- Automatic Django Admin access (superuser created during django migration)
- Pokedex user interaction through REST API docs provided by [Django Ninja](https://django-ninja.dev/) library

## Possible ideas for future enhancements
- PokeAPI data revalidation
- Faster asynchronous PokeAPI data fetch using async django command and `httpx` library
- Extended representation of PokeAPI resources in local database (new fields, relations, ...)

## Notable design choices
- Folder structure was divided into two packages - `djangoproject` and `pokecore`, in order to decouple the core logic of fetching data from PokeAPI from the presentation layer provided by Django app.
- `EvolutionChain` model was designed in a simple way, at the level of `PokemonSpecies`, not `Pokemon` and assuming maximum two stages of evolution (according to the info found on the Internet).
  In order to effectively store array data in evolution stages, `JSONField` was used.
- For exposing REST API endpoints, [Django Ninja](https://django-ninja.dev/) library was chosen instead of Django Rest Framework, because it's quite popular, maintained, and offers async support similar to FastAPI as well as overall ergonomics inspired by FastAPI.
- Selection of database that django app is interacting with is conveniently implemented using `USEDB` env variable (possible values `local` and `postgres`). This env variable is used in django's `settings.py`
- At deployment, database is provided as a `postgres` docker container, at development as a `sqlite` database
- UI was not built as my strong opinion is to use Django only for backend and delegate frontend to e.g. React or other full-fledged framework

## How to set up project for development

### 1. Install virtual environment
This project assumes Linux or WSL operating system and uses `uv` package manager. To properly install virtual environment, uv executable needs to be present in the system. If it's not, you can download and install it using curl:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

We use make command below, so if the make is not present in the system, install it using apt:
```
sudo apt install make
```

After cloning the repository, the virtual environment can be set up using the command:
```
uv sync
```

### 2. Run the Django app in development mode
The Django application can be run using Makefile command which will spin up local development server
```
make django
```
## How to deploy and run

### 1. Run dockerized application
Ensure `docker` command is installed on the system. Then run `docker-compose` command, which will spin up django app and postgres containers.
```
docker-compose up
```

### 2. API docs and usage:
API docs can be found at
```
http://127.0.0.1:8000/api/docs
```

### 3. Django Admin access for data preview:
Fetched data from PokeAPI can be previewed using `admin/admin` credentials at
```
http://127.0.0.1:8000/admin
```
