from ninja import NinjaAPI
from pokeapp.api import router

api = NinjaAPI(title="Pokedex API")

api.add_router("/", router, tags=["API endpoints"])
