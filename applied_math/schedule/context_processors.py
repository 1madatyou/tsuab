from .models import Schedule


def get_schedule_context(request):
    """Возвращает обьект расписания"""
    schedule = Schedule.objects.get()

    context = {'schedule': schedule}

    return context