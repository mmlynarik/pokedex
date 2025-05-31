from django.db import models
from pokeapp.models import Pokemon, PokemonAbility, PokemonForm, PokemonSpecies, PokemonStat, PokemonType

POKEMON_DJANGO_CLASSES: list[models.Model] = [
    PokemonType,
    PokemonStat,
    PokemonForm,
    Pokemon,
    PokemonSpecies,
    PokemonAbility,
]


def get_nonempty_pokemon_table_names() -> list[str]:
    objects = []
    for cls in POKEMON_DJANGO_CLASSES:
        if cls.objects.exists():
            objects.append(cls.__name__)
    return objects
