from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """
    Multiply two numeric values in templates:
        {{ value|multiply:arg }}
    Returns 0 on invalid input.
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        try:
            # if integer-like strings, try int
            return int(value) * int(arg)
        except Exception:
            return 0
