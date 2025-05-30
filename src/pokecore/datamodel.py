from pydantic import BaseModel


class PokemonType(BaseModel):
    name: str
