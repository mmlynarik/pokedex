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


class PokemonNotFound(Schema):
    msg: str
