from pathlib import Path
import requests
from pokedex.config import BASE_POKEMON_API_URL


def get_pokemon_types():
    types_url = Path(BASE_POKEMON_API_URL, "type")
    print(types_url)
    res = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    pokemon = res.json()


get_pokemon_types()
