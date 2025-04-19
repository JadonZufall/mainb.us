from django import template

register = template.Library()

@register.filter
def index(value, arg: str):
	return value[arg]

@register.filter
def index_default(value, arg: str):
	try:
		return value[arg]
	except IndexError:
		return None

@register.filter
def index_attr(value, arg: str):
	return getattr(value[arg.split(".", 1)[0]], arg.split(".", 1)[-1])