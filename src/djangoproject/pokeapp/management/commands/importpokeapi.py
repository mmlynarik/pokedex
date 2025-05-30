import logging

from django.core.management import BaseCommand
from pokeapp.models import Pokemon, PokemonForm, PokemonSpecies, PokemonType

from pokecore.pokeapi import get_pokemon_types

logger = logging.getLogger(__name__)


def get_existing_pokemon_objects() -> list[str]:
    objects = []
    if PokemonType.objects.exists():
        objects.append("PokemonType")
    if PokemonForm.objects.exists():
        objects.append("PokemonForm")
    if Pokemon.objects.exists():
        objects.append("Pokemon")
    if PokemonSpecies.objects.exists():
        objects.append("PokemonSpecies")
    return objects


class Command(BaseCommand):
    help = "Import basic Pokemon data from Pokemon API (pokeapi.co)"

    def handle(self, *args, **options):
        objects = get_existing_pokemon_objects()
        if objects:
            logger.info(
                f"The following tables are not empty: {objects}. Please delete all data before importing from Pokemon API"
            )
            return

        logger.info("Importing pokemon types")
        pokemon_types = [PokemonType(name=t.name) for t in get_pokemon_types()]
        PokemonType.objects.bulk_create(pokemon_types)
