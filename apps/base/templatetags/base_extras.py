from django import template
from django.shortcuts import resolve_url

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
	raise NotImplementedError("TODO: resolve_profile_picture_url")

@register.simple_tag
def resolve_profile_url(username: str):
	return resolve_url("authentication_user_profile", username)

@register.simple_tag
def length(value):
	if hasattr(value, "__len__"):
		return len(value)
	else:
		return 0

@register.filter
def length_add(value, arg: int):
	if hasattr(value, "__len__"):
		return len(value) + arg
	else:
		return arg