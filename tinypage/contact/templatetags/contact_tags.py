from django import template

register = template.Library()


@register.filter(is_safe=True)
def label_upper(field):
    return field.label_tag(contents=field.html_name.upper())
