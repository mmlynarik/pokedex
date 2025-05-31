from urllib.parse import urljoin

import requests

from pokecore.config import BASE_POKEMON_API_URL
from pokecore.pokeapi.datamodel import (
    Pokemon,
    PokemonAbility,
    PokemonAbilityValue,
    PokemonEvolutionChain,
    PokemonForm,
    PokemonSpecies,
    PokemonStat,
    PokemonStatValue,
    PokemonType,
)


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
    """Pokemons within each species share some properties, yet they represent standalone pokemon entities"""
    url = get_pokemon_resource_url("pokemon-species")
    index = requests.get(url).json()["results"]
    return [PokemonSpecies(name=i["name"]) for i in index]


def get_pokeapi_abilities() -> list[PokemonAbility]:
    url = get_pokemon_resource_url("ability")
    index = requests.get(url).json()["results"]
    return [PokemonAbility(name=i["name"]) for i in index]


def get_pokeapi_pokemon_entity_data() -> (
    tuple[list[Pokemon], list[PokemonStatValue], list[PokemonAbilityValue]]
):
    """To reduce network requests, pokemons, stat values and ability values data are fetched together"""
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
        stat_values = [
            PokemonStatValue(pokemon=pokemon_data["name"], stat=s["stat"]["name"], value=s["base_stat"])
            for s in pokemon_data["stats"]
        ]
        ability_values = [
            PokemonAbilityValue(
                pokemon=pokemon_data["name"], ability=a["ability"]["name"], is_hidden=a["is_hidden"]
            )
            for a in pokemon_data["abilities"]
        ]

    return pokemons, stat_values, ability_values


def get_pokeapi_pokemon_forms() -> list[PokemonForm]:
    """Each pokemon can either have one or multiple forms, of which exactly one is default"""
    pokemon_forms = []
    url = get_pokemon_resource_url("pokemon-form")
    index = requests.get(url).json()["results"]
    for i in index:
        pokemon_form_data = requests.get(i["url"]).json()
        pokemon_forms.append(
            PokemonForm(
                form=pokemon_form_data["name"],
                pokemon=pokemon_form_data["pokemon"]["name"],
                is_default=pokemon_form_data["is_default"],
            )
        )
    return pokemon_forms


def get_pokeapi_evolution_chains() -> list[PokemonEvolutionChain]:
    """There are min one and max three stages of evolution chain. Each pokemon belongs to exactly one chain"""
    pokemon_evolution_chains: list[PokemonEvolutionChain] = []
    url = get_pokemon_resource_url("evolution-chain")
    index = requests.get(url).json()["results"]
    for i in index:
        chain_data = requests.get(i["url"]).json()
        unevolved = chain_data["chain"]["species"]["name"]
        first_evolution = [e1["species"]["name"] for e1 in chain_data["chain"]["evolves_to"]]
        second_evolution = [
            e2["species"]["name"] for e1 in chain_data["chain"]["evolves_to"] for e2 in e1["evolves_to"]
        ]
        chain_members = [unevolved] + first_evolution + second_evolution
        pokemon_evolution_chains.extend(
            PokemonEvolutionChain(
                species=m,
                unevolved=unevolved,
                first_evolution=first_evolution,
                second_evolution=second_evolution,
            )
            for m in chain_members
        )
    return pokemon_evolution_chains
