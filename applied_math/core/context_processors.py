import locale

from django.utils import timezone


locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


def get_date_context(request):
    """Возвращает контекст с отформатированной сегодняшней датой"""
    
    today_datetime_data = []

    today_datetime_data.append(timezone.datetime.now().strftime("%d %B %Y")) 

    if timezone.datetime.now().isocalendar()[1] % 2:
        today_datetime_data.append('нечётная неделя')
    else:
        today_datetime_data.append('чётная неделя') 

    result = (', ').join(today_datetime_data)

    context = {}
    context.update({'today_formatted': result})

    return context

