import logging

from django.core.management import BaseCommand
from pokeapp.models import PokemonType

from pokecore.pokeapi import get_pokemon_types

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Import basic Pokemon data from Pokemon API (pokeapi.co)"

    def handle(self, *args, **options):
        pokemon_types = [PokemonType(name=t.name) for t in get_pokemon_types()]
        if not PokemonType.objects.exists():
            PokemonType.objects.bulk_create(pokemon_types)
