from ninja import NinjaAPI
from api.api import router

api = NinjaAPI()

api.add_router("/", router)
