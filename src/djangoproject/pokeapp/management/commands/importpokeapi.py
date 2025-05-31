import logging

from django.core.management import BaseCommand
from pokeapp.management.commands.common import get_nonempty_pokemon_table_names
from pokeapp.models import (
    Pokemon,
    PokemonAbility,
    PokemonAbilityValue,
    PokemonForm,
    PokemonSpecies,
    PokemonStat,
    PokemonStatValue,
    PokemonType,
)

from pokecore.pokeapi.client import (
    get_pokeapi_abilities,
    get_pokeapi_pokemon_entity_data,
    get_pokeapi_pokemon_forms,
    get_pokeapi_species,
    get_pokeapi_stats,
    get_pokeapi_types,
)

logger = logging.getLogger(__name__)


def import_pokemon_types():
    pokeapi_types = get_pokeapi_types()
    pokemon_types = [PokemonType(name=t.name) for t in pokeapi_types]
    PokemonType.objects.bulk_create(pokemon_types)


def import_pokemon_stats():
    pokeapi_stats = get_pokeapi_stats()
    pokemon_stats = [PokemonStat(name=s.name, is_battle_only=s.is_battle_only) for s in pokeapi_stats]
    PokemonStat.objects.bulk_create(pokemon_stats)


def import_pokemon_species():
    pokeapi_species = get_pokeapi_species()
    pokemon_species = [PokemonSpecies(name=s.name) for s in pokeapi_species]
    PokemonSpecies.objects.bulk_create(pokemon_species)


def import_pokemon_abilities():
    pokeapi_abilities = get_pokeapi_abilities()
    pokemon_abilities = [PokemonAbility(name=a.name) for a in pokeapi_abilities]
    PokemonAbility.objects.bulk_create(pokemon_abilities)


def import_pokemon_entity_data():
    """To reduce network requests, pokemons, stat values and ability values data are fetched together"""
    pokeapi_pokemons, pokeapi_stat_values, pokeapi_ability_values = get_pokeapi_pokemon_entity_data()
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

    stat_values = [
        PokemonStatValue(
            pokemon=Pokemon.objects.get(name=v.pokemon),
            value=v.value,
            stat=PokemonStat.objects.get(name=v.stat),
        )
        for v in pokeapi_stat_values
    ]
    PokemonStatValue.objects.bulk_create(stat_values)

    ability_values = [
        PokemonAbilityValue(
            pokemon=Pokemon.objects.get(name=v.pokemon),
            ability=PokemonAbility.objects.get(name=v.ability),
            is_hidden=v.is_hidden,
        )
        for v in pokeapi_ability_values
    ]
    PokemonAbilityValue.objects.bulk_create(ability_values)


def import_pokemon_forms():
    pokeapi_pokemon_forms = get_pokeapi_pokemon_forms()
    pokemon_forms = [
        PokemonForm(
            form=f.form,
            is_default=f.is_default,
            pokemon=Pokemon.objects.get(name=f.pokemon),
        )
        for f in pokeapi_pokemon_forms
    ]
    PokemonForm.objects.bulk_create(pokemon_forms)


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
        import_pokemon_types()

        logger.info("Importing PokemonStat data")
        import_pokemon_stats()

        logger.info("Importing PokemonSpecies data")
        import_pokemon_species()

        logger.info("Importing PokemonAbility data")
        import_pokemon_abilities()

        logger.info("Importing Pokemon, PokemonStatValue and PokemonAbilityValue data")
        import_pokemon_entity_data()

        logger.info("Importing PokemonForm data")
        import_pokemon_forms()
