from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def add_class(value, arg):
    end_tag = value.find('>')
    return value[:end_tag] + f' class="{arg}" ' + value[end_tag:]