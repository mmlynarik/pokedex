from pydantic import BaseModel


class PokemonType(BaseModel):
    name: str


class PokemonStat(BaseModel):
    name: str
    is_battle_only: bool


class PokemonSpecies(BaseModel):
    name: str


class PokemonAbility(BaseModel):
    name: str


class Pokemon(BaseModel):
    pokedex_no: int
    name: str
    types: list[str]
    species: str
    abilities: list[str]
    weight: int
    height: int
    base_experience: int
    is_default: bool


class PokemonForm(BaseModel):
    form: str
    pokemon: str
    is_default: bool


class PokemonStatValue(BaseModel):
    pokemon: str
    stat: str
    value: int
