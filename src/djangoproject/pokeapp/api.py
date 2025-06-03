from ninja import Field, FilterSchema, Query, Router
from pokeapp.datamodel import (
    EvolutionChain,
    PokemonDetail,
    PokemonNotFound,
    PokemonsList,
    PokemonStatsCompare,
)
from pokeapp.models import Pokemon, PokemonEvolutionChain, PokemonForm
from pokeapp.utils import get_not_found_error_msg, get_pokemon_detail_from_form, get_stats_values_for_pokemon

router = Router()


@router.get(
    "/pokemon/{name}",
    response={200: PokemonDetail, 404: PokemonNotFound},
    summary="Retrieve Pokemon or PokemonForm detail from Pokedex",
)
def get_pokemon_detail(request, name: str):
    pokemon_form = PokemonForm.objects.filter(form=name).first()
    if not pokemon_form:
        return 404, PokemonNotFound(msg=get_not_found_error_msg(name))

    return get_pokemon_detail_from_form(pokemon_form)


class PokemonFilterSchema(FilterSchema):
    types: str | None = Field(None, q="__name")
    abilities: str | None = Field(None, q="__ability__name")


@router.get(
    "/pokemon",
    response={200: PokemonsList},
    summary="Retrieve list of all or filtered Pokemons and PokemonForms from Pokedex",
)
def get_pokemon_list(request, filters: PokemonFilterSchema = Query(...)):
    pokemons = Pokemon.objects.all()
    filtered_pokemons = filters.filter(pokemons)
    pokemon_forms = PokemonForm.objects.filter(pokemon__in=filtered_pokemons)
    return PokemonsList(
        count=pokemon_forms.count(),
        pokemons=[get_pokemon_detail_from_form(pokemon_form) for pokemon_form in pokemon_forms],
    )


@router.get(
    "/pokemon-compare/{first}/{second}",
    response={200: PokemonStatsCompare, 404: PokemonNotFound},
    summary="Compare stats of two Pokemons",
)
def get_pokemon_stats_comparison(request, first: str, second: str):
    first_pokemon = Pokemon.objects.filter(name=first).first()
    second_pokemon = Pokemon.objects.filter(name=second).first()

    if not first_pokemon:
        return 404, PokemonNotFound(msg=get_not_found_error_msg(first))
    if not second_pokemon:
        return 404, PokemonNotFound(msg=get_not_found_error_msg(second))

    first_stats = get_stats_values_for_pokemon(first_pokemon)
    second_stats = get_stats_values_for_pokemon(second_pokemon)

    return PokemonStatsCompare(
        first=first,
        second=second,
        hp=[first_stats["hp"], second_stats["hp"]],
        attack=[first_stats["attack"], second_stats["attack"]],
        defense=[first_stats["defense"], second_stats["defense"]],
        special_attack=[first_stats["special-attack"], second_stats["special-attack"]],
        special_defense=[first_stats["special-defense"], second_stats["special-defense"]],
        speed=[first_stats["speed"], second_stats["speed"]],
    )


@router.get(
    "/pokemon-evolution-chain/{name}",
    response={200: EvolutionChain, 404: PokemonNotFound},
    summary="Display Pokemon's or PokemonForm's evolution chain based on its species",
)
def get_evolution_chain(request, name: str):
    pokemon_form = PokemonForm.objects.filter(form=name).first()

    if not pokemon_form:
        return 404, PokemonNotFound(msg=get_not_found_error_msg(name))

    species = pokemon_form.pokemon.species
    evolution_chain = PokemonEvolutionChain.objects.get(species=species)

    return EvolutionChain(
        unevolved=evolution_chain.unevolved,
        first_evolution=evolution_chain.first_evolution,
        second_evolution=evolution_chain.second_evolution,
    )
