from typing import Any

from pokeapp.models import Pokemon, PokemonStatValue

StatsValues = list[dict[str, Any]]


def get_not_found_error_msg(name: str) -> str:
    return f"Pokemon {name} was not found. Check the spelling and try again. In case of composite pokemon names, use hyphen (e.g. wormadam-plant)"


def get_stats_values_for_pokemon(pokemon: Pokemon):
    first_stats = PokemonStatValue.objects.filter(pokemon=pokemon).values("stat__name", "value")
    return {s["stat__name"]: s["value"] for s in first_stats}
