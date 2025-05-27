# Pokedex API Django Project

## How to set up project for development

### 1. Install virtual environment
This project assumes Linux or WSL operating system and uses `uv` package manager. To properly install virtual environment, uv executable needs to be present in the system. If it's not, you can download and install it using curl:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After cloning the repository, the virtual environment can be set up using the command:
```
uv sync
```

## 2. Run the Django app in development mode
The Django application can be run using Makefile command which will spin up local development server
```
make django
```
## How to run 

### 1. Run dockerized application
Ensure `docker` command is installed on the system. Then run
```
docker-compose up
```

### 2. API docs and usage:
API docs can be found at
```
http://127.0.0.1:8000/docs
```
