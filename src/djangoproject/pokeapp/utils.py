from typing import Any

from pokeapp.datamodel import PokemonDetail
from pokeapp.models import Pokemon, PokemonForm, PokemonStatValue

StatsValues = list[dict[str, Any]]


def get_not_found_error_msg(name: str) -> str:
    return f"Pokemon {name} was not found. Check the spelling and try again. In case of composite pokemon names, use hyphen (e.g. wormadam-plant)"


def get_stats_values_for_pokemon(pokemon: Pokemon):
    first_stats = PokemonStatValue.objects.filter(pokemon=pokemon).values("stat__name", "value")
    return {s["stat__name"]: s["value"] for s in first_stats}


def get_pokemon_detail_from_form(pokemon_form: PokemonForm) -> PokemonDetail:
    stats = get_stats_values_for_pokemon(pokemon_form.pokemon)
    return PokemonDetail(
        pokedex_no=pokemon_form.pokemon.pokedex_no,
        name=pokemon_form.form,
        types=pokemon_form.pokemon.types.all().values_list("name", flat=True),
        species=pokemon_form.pokemon.species.name,
        weight=pokemon_form.pokemon.weight,
        height=pokemon_form.pokemon.height,
        base_experience=pokemon_form.pokemon.base_experience,
        is_species_default=pokemon_form.pokemon.is_default,
        is_default_form=pokemon_form.is_default,
        form_or_variety="variety" if pokemon_form.form == pokemon_form.pokemon.name else "form",
        stats=stats,
    )
