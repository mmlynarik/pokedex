from ninja import Router
from pokeapp.models import PokemonForm

router = Router()


@router.get("/forms/{form}")
def get_pokemon_form(request, pokemon_form: str):
    PokemonForm.objects.filter(name=pokemon_form)

    # return [{"id": p.pk, "pokedex_no": p.pokedex_no} for p in Pokemon.objects.all()]
