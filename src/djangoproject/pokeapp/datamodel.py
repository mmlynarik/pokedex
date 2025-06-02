from typing import Literal

from ninja import Schema


class PokemonDetail(Schema):
    pokedex_no: int
    name: str
    types: list[str]
    species: str
    weight: int
    height: int
    base_experience: int
    is_default_form: bool
    is_species_default: bool
    form_or_variety: Literal["form", "variety"]
    stats: dict[str, int]
    abilities: dict[str, str]


class PokemonsList(Schema):
    count: int
    pokemons: list[PokemonDetail]


class PokemonStatsCompare(Schema):
    first: str
    second: str
    hp: tuple[int, int]
    attack: tuple[int, int]
    defense: tuple[int, int]
    special_attack: tuple[int, int]
    special_defense: tuple[int, int]
    speed: tuple[int, int]


class PokemonNotFound(Schema):
    msg: str
