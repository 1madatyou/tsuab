import locale

from django.template.defaultfilters import date as _date
from django.utils import timezone
from django.utils import translation
from django.utils.translation import gettext_lazy as _


def get_date_context(request):
    """Возвращает контекст с отформатированной сегодняшней датой"""
    week_type = (
        _("чётная неделя")
        if timezone.datetime.now().isocalendar()[1] % 2 == 0
        else _("нечётная неделя")
    )
    today_datetime = _date(timezone.datetime.now(), "d E Y")

    print(translation.get_language())
    print(str(week_type))

    context = {}
    context.update({"week_type": week_type, "today_datetime": today_datetime})

    return context
