from ninja import Router
from api.models import Pokemon

router = Router()


@router.get("/events")
def list_events(request):
    return [{"id": p.pk, "pokedex_no": p.pokedex_no} for p in Pokemon.objects.all()]
