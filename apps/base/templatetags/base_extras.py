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

@register.filter
def concat(value, arg: str):
	return str(value) + str(arg)

@register.filter
def prefix(value, arg: str):
	return str(arg) + str(value)

@register.simple_tag
def resolve_profile_picture_url(username: str):
	return "{% static 'img/avatar_placeholder.jpg' %}"

@register.simple_tag
def resolve_profile_url(username: str):
	return f"/u/{username}/" if username else "/u/"