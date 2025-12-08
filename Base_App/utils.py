from .models import CMSContent


def cms(page, key, default=""):
    try:
        return CMSContent.objects.get(page=page, key=key).value
    except CMSContent.DoesNotExist:
        return default
