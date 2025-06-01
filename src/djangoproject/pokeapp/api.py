from ninja import Router
from pokeapp.datamodel import PokemonDetail, PokemonNotFound, PokemonStatsCompare
from pokeapp.models import Pokemon, PokemonForm, PokemonStatValue
from pokeapp.utils import get_not_found_error_msg, get_stat_values_from_all_stats

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

    first_stats = PokemonStatValue.objects.filter(pokemon=first_pokemon).values("stat__name", "value")
    second_stats = PokemonStatValue.objects.filter(pokemon=second_pokemon).values("stat__name", "value")

    return PokemonStatsCompare(
        first=first,
        second=second,
        hp=get_stat_values_from_all_stats("hp", first_stats, second_stats),
        attack=get_stat_values_from_all_stats("attack", first_stats, second_stats),
        defense=get_stat_values_from_all_stats("defense", first_stats, second_stats),
        special_attack=get_stat_values_from_all_stats("special-attack", first_stats, second_stats),
        special_defense=get_stat_values_from_all_stats("special-defense", first_stats, second_stats),
        speed=get_stat_values_from_all_stats("speed", first_stats, second_stats),
    )
