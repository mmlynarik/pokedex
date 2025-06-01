from ninja import Router, Schema
from pokeapp.models import Pokemon, PokemonForm

router = Router()


class PokemonDetail(Schema):
    pokedex_no: int
    name: str
    types: list[str]
    weight: int
    height: int
    is_default: bool


class PokemonNotFound(Schema):
    msg: str


@router.get(
    "/pokemons/{name}",
    response={200: PokemonDetail, 404: PokemonNotFound},
    summary="Retrieve one Pokemon or PokemonForm from Pokedex",
)
def get_pokemon_form(request, name: str):
    pokemon_form = PokemonForm.objects.filter(form=name).first()
    if not pokemon_form:
        return 404, PokemonNotFound(msg=f"Pokemon {name} was not found. Check the spelling and try again.")

    pokemon = Pokemon.objects.get(name=pokemon_form.form)
    return {
        "pokedex_no": pokemon.pokedex_no,
        "name": pokemon_form.form,
        "types": pokemon.types.all().values_list("name", flat=True),
        "weight": pokemon.weight,
        "height": pokemon.height,
        "is_default": pokemon_form.is_default,
    }
