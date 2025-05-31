import logging

from django.core.management import BaseCommand
from pokeapp.management.commands.common import get_nonempty_pokemon_table_names
from pokeapp.models import Pokemon, PokemonAbility, PokemonForm, PokemonSpecies, PokemonStat, PokemonType

from pokecore.pokeapi.client import (
    get_pokeapi_abilities,
    get_pokeapi_pokemon_forms,
    get_pokeapi_pokemons,
    get_pokeapi_species,
    get_pokeapi_stats,
    get_pokeapi_types,
)

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
        pokeapi_stats = get_pokeapi_stats()
        pokemon_stats = [PokemonStat(name=s.name, is_battle_only=s.is_battle_only) for s in pokeapi_stats]
        PokemonStat.objects.bulk_create(pokemon_stats)

        logger.info("Importing PokemonSpecies data")
        pokeapi_species = get_pokeapi_species()
        pokemon_species = [PokemonSpecies(name=s.name) for s in pokeapi_species]
        PokemonSpecies.objects.bulk_create(pokemon_species)

        logger.info("Importing PokemonAbility data")
        pokeapi_abilities = get_pokeapi_abilities()
        pokemon_abilities = [PokemonAbility(name=a.name) for a in pokeapi_abilities]
        PokemonAbility.objects.bulk_create(pokemon_abilities)

        logger.info("Importing Pokemon data")
        pokeapi_pokemons = get_pokeapi_pokemons()
        for p in pokeapi_pokemons:
            pokemon = Pokemon(
                pokedex_no=p.pokedex_no,
                name=p.name,
                height=p.height,
                weight=p.weight,
                base_experience=p.base_experience,
                is_default=p.is_default,
                species=PokemonSpecies.objects.get(name=p.species),
            )
            pokemon.save()
            pokemon.types.add(*PokemonType.objects.filter(name__in=p.types))
            pokemon.abilities.add(*PokemonAbility.objects.filter(name__in=p.abilities))

        logger.info("Importing PokemonForm data")
        pokeapi_pokemon_forms = get_pokeapi_pokemon_forms()
        for p in pokeapi_pokemon_forms:
            pokemon_form = PokemonForm(
                name=p.name,
                form_name=p.form_name,
                is_default=p.is_default,
                pokemon=Pokemon.objects.get(name=p.pokemon),
            )
            pokemon_form.save()
