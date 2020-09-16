from django import template

register = template.Library()


@register.filter(name='line')
def letter(values, l):
    return values, l


@register.filter(name='column')
def number(values_l, c):
    values, l = values_l
    if values:
        return values[l + c]
    else:
        return ""
