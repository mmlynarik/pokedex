from urllib.parse import urljoin

import requests

from pokecore.config import BASE_POKEMON_API_URL
from pokecore.datamodel import PokemonAbility, PokemonSpecies, PokemonStat, PokemonType


def get_limit_query_param(max=100_000) -> str:
    return f"?limit={max}"


def get_pokemon_resource_url(resource: str) -> str:
    url = urljoin(BASE_POKEMON_API_URL, resource)
    query = get_limit_query_param()
    unlimited_url = urljoin(url, query)
    return unlimited_url


def get_pokeapi_types() -> list[PokemonType]:
    url = get_pokemon_resource_url("type")
    data = requests.get(url).json()
    return [PokemonType(name=r["name"]) for r in data["results"]]


def get_pokeapi_stats() -> list[PokemonStat]:
    stats = []
    url = get_pokemon_resource_url("stat")
    summary = requests.get(url).json()["results"]
    for s in summary:
        stat_data = requests.get(s["url"]).json()
        stats.append(PokemonStat(name=stat_data["name"], is_battle_only=stat_data["is_battle_only"]))
    return stats


def get_pokeapi_species() -> list[PokemonSpecies]:
    url = get_pokemon_resource_url("pokemon-species")
    data = requests.get(url).json()
    return [PokemonSpecies(name=r["name"]) for r in data["results"]]


def get_pokeapi_abilities() -> list[PokemonAbility]:
    url = get_pokemon_resource_url("ability")
    data = requests.get(url).json()
    return [PokemonAbility(name=r["name"]) for r in data["results"]]
