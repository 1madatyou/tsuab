import re
from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext

from django.utils import translation


register = template.Library()

@register.filter(name='urlize')
def urlize(value):
    url_pattern = re.compile(r'(https?://[^\s]+)')
    return mark_safe(url_pattern.sub(r'<a href="\1" target="_blank">\1</a>', value))

@register.filter
def ru_plural(value, variants):
    variants = variants.split(",")
    value = abs(int(value))

    print(translation.get_language())

    if value % 10 == 1 and value % 100 != 11:
        variant = 0
    elif value % 10 >= 2 and value % 10 <= 4 and \
            (value % 100 < 10 or value % 100 >= 20):
        variant = 1
    else:
        variant = 2

    print(str(_(variants[variant])))

    return _(variants[variant])