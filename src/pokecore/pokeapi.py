from urllib.parse import urljoin

import requests

from pokecore.config import BASE_POKEMON_API_URL
from pokecore.datamodel import PokemonType


def get_limit_query_param() -> str:
    return "?limit=100000"


def get_pokemon_types_url() -> str:
    types_url = urljoin(BASE_POKEMON_API_URL, "type")
    limit_query = get_limit_query_param()
    unlimited_url = urljoin(types_url, limit_query)
    return unlimited_url


def get_pokemon_types() -> list[PokemonType]:
    types_url = get_pokemon_types_url()
    data = requests.get(types_url).json()
    return [PokemonType(name=i["name"]) for i in data["results"]]
