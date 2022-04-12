from django import template
register = template.Library()


def do_subtract(value, arg):
    if value is None or arg is None:
        return 0.000
    else:
        return float(value) - float(arg)

register.filter("do_subtract", do_subtract)
