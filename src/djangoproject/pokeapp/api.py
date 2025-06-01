from ninja import Router
from pokeapp.datamodel import PokemonDetail, PokemonNotFound
from pokeapp.models import PokemonForm

router = Router()


@router.get(
    "/pokemon/{name}",
    response={200: PokemonDetail, 404: PokemonNotFound},
    summary="Retrieve Pokemon or PokemonForm detail from Pokedex",
)
def get_pokemon_detail(request, name: str):
    pokemon_form = PokemonForm.objects.filter(form=name).first()
    if not pokemon_form:
        return 404, PokemonNotFound(
            msg=f"Pokemon {name} was not found. Check the spelling and try again. In case of composite pokemon names, use hyphen (e.g. wormadam-plant)"
        )

    return {
        "pokedex_no": pokemon_form.pokemon.pokedex_no,
        "name": pokemon_form.form,
        "types": pokemon_form.pokemon.types.all().values_list("name", flat=True),
        "species": pokemon_form.pokemon.species.name,
        "weight": pokemon_form.pokemon.weight,
        "height": pokemon_form.pokemon.height,
        "base_experience": pokemon_form.pokemon.base_experience,
        "is_species_default": pokemon_form.pokemon.is_default,
        "is_default_form": pokemon_form.is_default,
        "form_or_variety": "variety" if pokemon_form.form == pokemon_form.pokemon.name else "form",
    }


@router.get(
    "/pokemon",
    response={200: list[PokemonDetail]},
    summary="Retrieve list of all Pokemons and PokemonForms from Pokedex",
)
def get_pokemon_list(request):
    pokemon_forms = PokemonForm.objects.all()
    return [
        {
            "pokedex_no": pokemon_form.pokemon.pokedex_no,
            "name": pokemon_form.form,
            "types": pokemon_form.pokemon.types.all().values_list("name", flat=True),
            "species": pokemon_form.pokemon.species.name,
            "weight": pokemon_form.pokemon.weight,
            "height": pokemon_form.pokemon.height,
            "base_experience": pokemon_form.pokemon.base_experience,
            "is_species_default": pokemon_form.pokemon.is_default,
            "is_default_form": pokemon_form.is_default,
            "form_or_variety": "variety" if pokemon_form.form == pokemon_form.pokemon.name else "form",
        }
        for pokemon_form in pokemon_forms
    ]
