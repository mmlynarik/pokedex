from pprint import pprint
from typing import Any
from urllib.parse import urljoin

import requests

from pokecore.config import BASE_POKEMON_API_URL


def get_limit_query_param() -> str:
    return "?limit=100000"


def get_pokemon_types_url() -> str:
    types_url = urljoin(BASE_POKEMON_API_URL, "type")
    limit_query = get_limit_query_param()
    unlimited_url = urljoin(types_url, limit_query)
    return unlimited_url


def get_pokemon_types() -> dict[str, Any]:
    types_url = get_pokemon_types_url()
    data = requests.get(types_url).json()
    return data


pprint(get_pokemon_types())
