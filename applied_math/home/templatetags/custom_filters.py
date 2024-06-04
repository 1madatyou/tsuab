import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='urlize')
def urlize(value):
    url_pattern = re.compile(r'(https?://[^\s]+)')
    return mark_safe(url_pattern.sub(r'<a href="\1" target="_blank">\1</a>', value))