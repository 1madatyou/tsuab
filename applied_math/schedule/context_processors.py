from .models import Schedule


def get_schedule_context(request):
    """Возвращает обьект расписания"""
    try:
        schedule = Schedule.objects.get()
    except Schedule.DoesNotExist:
        schedule = None
        
    context = {'schedule': schedule}

    return context