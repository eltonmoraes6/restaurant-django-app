from django import template

from Base_App.models import PageSection

register = template.Library()

@register.simple_tag
def cms(page, section, field="content", default=""):
    try:
        data = PageSection.objects.get(page=page, section=section)
        return getattr(data, field) or default
    except PageSection.DoesNotExist:
        return default
