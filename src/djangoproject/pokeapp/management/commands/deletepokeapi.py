import logging

from django.core.management import BaseCommand
from pokeapp.management.commands.common import POKEMON_DJANGO_CLASSES

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Delete all previously imported Pokemon data from Pokemon API (pokeapi.co)"

    def handle(self, *args, **options):
        for cls in POKEMON_DJANGO_CLASSES:
            if cls.objects.exists():
                logger.info(f"Deleting {cls.__name__} data")
                cls.objects.all().delete()
