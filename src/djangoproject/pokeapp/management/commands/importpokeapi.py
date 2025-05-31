import logging

from django.core.management import BaseCommand
from pokeapp.management.commands.common import get_nonempty_pokemon_table_names
from pokeapp.models import PokemonStat, PokemonType

from pokecore.pokeapi import get_pokeapi_types, get_pokemon_stats

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Import basic Pokemon data from Pokemon API (pokeapi.co)"

    def handle(self, *args, **options):
        names = get_nonempty_pokemon_table_names()
        if names:
            logger.info(
                f"The following tables are not empty: {names}. Please delete all data before importing from Pokemon API"
            )
            return

        logger.info("Importing PokemonType data")
        pokeapi_types = get_pokeapi_types()
        pokemon_types = [PokemonType(name=t.name) for t in pokeapi_types]
        PokemonType.objects.bulk_create(pokemon_types)

        logger.info("Importing PokemonStat data")
        pokeapi_stats = get_pokemon_stats()
        pokemon_stats = [PokemonStat(name=s.name, is_battle_only=s.is_battle_only) for s in pokeapi_stats]
        PokemonStat.objects.bulk_create(pokemon_stats)
