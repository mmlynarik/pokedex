from ninja import NinjaAPI
from api.api import router

api = NinjaAPI(title="Pokedex API")

api.add_router("/", router, tags=["API endpoints"])
