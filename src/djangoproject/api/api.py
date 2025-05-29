from ninja import Router
from api.models import Employee

router = Router()


@router.get("/events")
def list_events(request):
    return [{"id": e.pk, "last_name": e.last_name} for e in Employee.objects.all()]
