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
