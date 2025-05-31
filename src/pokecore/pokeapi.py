from urllib.parse import urljoin

import requests

from pokecore.config import BASE_POKEMON_API_URL
from pokecore.datamodel import Pokemon, PokemonAbility, PokemonSpecies, PokemonStat, PokemonType


def get_limit_query_param(max=100_000) -> str:
    return f"?limit={max}"


def get_pokemon_resource_url(resource: str) -> str:
    url = urljoin(BASE_POKEMON_API_URL, resource)
    query = get_limit_query_param()
    unlimited_url = urljoin(url, query)
    return unlimited_url


def get_pokeapi_types() -> list[PokemonType]:
    url = get_pokemon_resource_url("type")
    index = requests.get(url).json()["results"]
    return [PokemonType(name=i["name"]) for i in index]


def get_pokeapi_stats() -> list[PokemonStat]:
    stats = []
    url = get_pokemon_resource_url("stat")
    index = requests.get(url).json()["results"]
    for i in index:
        stat_data = requests.get(i["url"]).json()
        stats.append(PokemonStat(name=stat_data["name"], is_battle_only=stat_data["is_battle_only"]))
    return stats


def get_pokeapi_species() -> list[PokemonSpecies]:
    url = get_pokemon_resource_url("pokemon-species")
    index = requests.get(url).json()["results"]
    return [PokemonSpecies(name=i["name"]) for i in index]


def get_pokeapi_abilities() -> list[PokemonAbility]:
    url = get_pokemon_resource_url("ability")
    index = requests.get(url).json()["results"]
    return [PokemonAbility(name=i["name"]) for i in index]


def get_pokeapi_pokemon() -> list[Pokemon]:
    pokemons = []
    url = get_pokemon_resource_url("pokemon")
    index = requests.get(url).json()["results"]
    for i in index:
        pokemon_data = requests.get(i["url"]).json()
        pokemons.append(
            Pokemon(
                pokedex_no=pokemon_data["id"],
                name=pokemon_data["name"],
                weight=pokemon_data["weight"],
                height=pokemon_data["height"],
                is_default=pokemon_data["is_default"],
                base_experience=pokemon_data["base_experience"],
                species=pokemon_data["species"]["name"],
                abilities=[a["ability"]["name"] for a in pokemon_data["abilities"]],
                types=[t["type"]["name"] for t in pokemon_data["types"]],
            )
        )
    return pokemons
