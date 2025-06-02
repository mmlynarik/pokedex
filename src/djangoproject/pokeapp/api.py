from ninja import Router
from pokeapp.datamodel import PokemonDetail, PokemonNotFound, PokemonStatsCompare
from pokeapp.models import Pokemon, PokemonForm
from pokeapp.utils import get_not_found_error_msg, get_stats_values_for_pokemon

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

    return pokemon_form.get_pokemon_detail()


@router.get(
    "/pokemon",
    response={200: list[PokemonDetail]},
    summary="Retrieve list of all Pokemons and PokemonForms from Pokedex",
)
def get_pokemon_list(request):
    pokemon_forms = PokemonForm.objects.all()
    return [pokemon_form.get_pokemon_detail() for pokemon_form in pokemon_forms]


@router.get(
    "/pokemon-compare/{first}/{second}",
    response={200: PokemonStatsCompare, 404: PokemonNotFound},
    summary="Compare stats of two Pokemons",
)
def compare_pokemon_stats(request, first: str, second: str):
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
